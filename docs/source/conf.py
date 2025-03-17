# -- 项目信息 -----------------------------------------------------

project = 'Simon\'s Blog'
copyright = '2023, Simon CHOU'
author = 'Simon CHOU'

# -- 一般配置 -----------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'recommonmark',
    'sphinx_markdown_tables',
]

templates_path = ['_templates']
exclude_patterns = []
language = 'zh_CN'

# -- HTML 输出选项 -------------------------------------------------

html_theme = 'sphinx_rtd_theme'  # 使用 Read the Docs 主题
html_static_path = ['_static']
html_title = 'Simon\'s Blog'
html_favicon = '_static/favicon.ico'  # 如果有的话

# 支持 Markdown
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# 设置主页
master_doc = 'index'
