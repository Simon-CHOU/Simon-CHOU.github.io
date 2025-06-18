# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Simon's Wiki"
author = 'Simon CHOU'
copyright = '2025, Simon CHOU'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'  # 使用 Read the Docs 主题
html_static_path = ['_static']

# -- 语言设置 -----------------------------------------------------------------
language = 'zh_CN'

# -- 文件后缀设置 ------------------------------------------------------------
source_suffix = '.rst'

# -- 主题配置 -----------------------------------------------------------------
html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'includehidden': True,
    'titles_only': False
}

# -- 其他配置 -----------------------------------------------------------------
html_title = project
html_short_title = "Simon's Wiki"
html_show_sourcelink = False
html_show_sphinx = False
html_show_copyright = True