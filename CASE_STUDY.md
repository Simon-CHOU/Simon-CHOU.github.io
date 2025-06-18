# Sphinx 文档项目 Case Study

## 项目概述

本项目是一个基于 Sphinx 的个人博客/Wiki 网站，使用 Read the Docs 主题，支持中文内容，并通过 GitHub Pages 进行部署。

## 今日完成的任务总结

### 1. 主题恢复与配置
- **问题**：需要将文档主题从 alabaster 恢复为 sphinx_rtd_theme
- **解决方案**：
  - 修改 `_sources/conf.py` 中的 `html_theme` 设置
  - 安装缺失的 `sphinx_rtd_theme` 包
  - 恢复主题相关配置选项
- **结果**：成功恢复 Read the Docs 主题样式

### 2. 版权信息更新
- **问题**：需要将版权年份从 2024 更新为 2025
- **解决方案**：修改 `conf.py` 中的 `copyright` 字段
- **结果**：网站底部版权信息成功更新

### 3. 项目清理
- **问题**：清理项目中非必要的文件和目录
- **解决方案**：
  - 分析项目结构，识别 Sphinx 相关文件
  - 保留必要的 `.nojekyll` 文件（用于 GitHub Pages）
  - 创建 `.gitignore` 文件，排除不必要的文件
- **结果**：项目结构更加清晰，版本控制更加规范

### 4. 项目重命名
- **问题**：将博客标题从 "Simon CHOU 的个人博客" 更改为 "Simon's Wiki"
- **解决方案**：
  - 修改 `conf.py` 中的 `project` 和 `html_short_title` 设置
  - 重新构建文档
- **结果**：网站标题成功更新为 "Simon's Wiki"

### 5. 文件作用分析
- **问题**：确认 `.nojekyll` 文件的必要性
- **解决方案**：分析文件作用，确认其对 GitHub Pages 部署的重要性
- **结果**：保留该文件以确保 Sphinx 生成的下划线开头目录能正常访问

## 关键学习点

1. **Sphinx 配置管理**：`conf.py` 是核心配置文件，控制主题、标题、版权等关键信息
2. **依赖管理**：主题切换时需要确保相关包已安装
3. **GitHub Pages 兼容性**：`.nojekyll` 文件对于 Sphinx 项目在 GitHub Pages 上的正确显示至关重要
4. **项目结构理解**：区分源文件（`_sources/`）和生成文件的重要性

---

# Sphinx 博客管理手册

## 项目结构说明

```
Simon-CHOU.github.io/
├── _sources/           # Sphinx 源文件目录
│   ├── conf.py        # 主配置文件
│   ├── index.rst      # 主页源文件
│   ├── blog/          # 博客文章源文件
│   ├── code-diary/    # 代码日记源文件
│   └── about/         # 关于页面源文件
├── _static/           # 静态资源（CSS、JS、图片等）
├── blog/              # 生成的博客页面
├── code-diary/        # 生成的代码日记页面
├── about/             # 生成的关于页面
├── index.html         # 生成的主页
└── .nojekyll          # GitHub Pages 配置文件
```

## 博文管理操作指南

### 1. 添加新博文

#### 步骤 1：创建源文件
在 `_sources/blog/` 目录下创建新的 `.rst` 文件：

```bash
# 进入源文件目录
cd _sources/blog/

# 创建新博文文件
touch 新博文标题.rst
```

#### 步骤 2：编写内容
使用 reStructuredText 格式编写博文：

```rst
新博文标题
==========

发布日期：2025-01-XX

简介
----

这里是博文的简介内容。

正文内容
--------

这里是博文的正文内容。

代码示例
--------

.. code-block:: python

   def hello_world():
       print("Hello, World!")

总结
----

这里是总结内容。
```

#### 步骤 3：更新索引
编辑 `_sources/blog/index.rst`，添加新博文到目录树：

```rst
.. toctree::
   :maxdepth: 2

   现有博文1
   现有博文2
   新博文标题
```

### 2. 修改现有博文

直接编辑 `_sources/blog/` 目录下对应的 `.rst` 文件即可。

### 3. 删除博文

#### 步骤 1：删除源文件
```bash
rm _sources/blog/要删除的博文.rst
```

#### 步骤 2：更新索引
从 `_sources/blog/index.rst` 中移除对应的条目。

### 4. 重新编译和发布

#### 方法 1：使用 Sphinx 命令
```bash
# 激活虚拟环境（如果使用）
myenv\Scripts\activate

# 清理旧的构建文件（可选）
sphinx-build -E -a -b html _sources .

# 或者常规构建
sphinx-build -b html _sources .
```

#### 方法 2：使用 Make（如果有 Makefile）
```bash
make clean
make html
```

### 5. 预览和部署

#### 本地预览
```bash
# 启动本地服务器
python -m http.server 8000

# 在浏览器中访问
# http://localhost:8000
```

#### 部署到 GitHub Pages
```bash
# 添加所有更改
git add .

# 提交更改
git commit -m "添加新博文：博文标题"

# 推送到远程仓库
git push origin main
```

## 常用配置修改

### 修改网站标题
编辑 `_sources/conf.py`：
```python
project = '新的网站标题'
html_title = project
html_short_title = '简短标题'
```

### 修改主题
编辑 `_sources/conf.py`：
```python
html_theme = 'sphinx_rtd_theme'  # 或其他主题
```

### 添加新的顶级页面
1. 在 `_sources/` 下创建新目录和 `index.rst` 文件
2. 在 `_sources/index.rst` 的 toctree 中添加新页面
3. 重新构建

## 故障排除

### 构建失败
- 检查 `.rst` 文件语法是否正确
- 确认所有引用的文件都存在
- 查看构建日志中的具体错误信息

### 样式问题
- 确认主题包已正确安装
- 检查 `_static/` 目录中的自定义 CSS 文件
- 清理缓存后重新构建

### GitHub Pages 显示问题
- 确认 `.nojekyll` 文件存在
- 检查仓库设置中的 Pages 配置
- 确认推送到正确的分支

## 最佳实践

1. **定期备份**：定期提交代码到 Git 仓库
2. **本地测试**：发布前先在本地预览效果
3. **文件命名**：使用有意义的文件名，避免特殊字符
4. **内容组织**：合理使用目录结构组织内容
5. **版本控制**：使用 `.gitignore` 排除生成文件和临时文件