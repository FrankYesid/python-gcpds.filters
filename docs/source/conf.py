# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
sys.path.insert(0, os.path.abspath('exts'))


# -- Project information -----------------------------------------------------

project = 'filters'
copyright = '2020, GCPDS - filters'
author = 'GCPDS'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',

    'sphinx.ext.autosectionlabel',
    'sphinx.ext.todo',
    'IPython.sphinxext.ipython_console_highlighting',
]

naoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = True
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The master toctree document.
master_doc = 'index'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_theme_options = {
    'page_width': '1080px',
    'sidebar_width': '310px',

    # 'fixed_sidebar': True,

    # 'show_relbars': True,
    # 'show_relbar_bottom': True,


    # 'github_user': 'bitprophet',
    # 'github_repo': 'alabaster',
}


html_sidebars = {
    '**': [
        #'about.html',
        'sidebar.html',
        # 'globaltoc.html',

        'navigation.html',
        'relations.html',
        # sourcelink.html
        'searchbox.html',
        # 'donate.html',
    ]
}

htmlhelp_basename = 'GCPDS_filters_doc'


autodoc_mock_imports = [

    'IPython',
    
    # 'base_server.WSHandler_Serial',
    # 'base_server.WSHandler_WiFi',
    # 'ws.base_server',

]

todo_include_todos = True

# html_logo = '_static/logo.svg'
# html_favicon = '_static/favico.ico'


def setup(app):
    app.add_css_file("custom.css")


highlight_language = 'none'
html_sourcelink_suffix = ''

# suppress_warnings = [
    # 'nbsphinx',
# ]

nbsphinx_execute_arguments = [
    "--InlineBackend.figure_formats={'svg', 'pdf'}",
    "--InlineBackend.rc={'figure.dpi': 96}",
]

nbsphinx_execute = 'never'
# nbsphinx_input_prompt = 'In [%s]:'
# nbsphinx_output_prompt = 'Out[%s]:'
nbsphinx_kernel_name = 'python3'


notebooks_dir = 'notebooks'

notebooks_list = os.listdir(os.path.join(
    os.path.abspath(os.path.dirname(__file__)), notebooks_dir))

notebooks = []
for notebook in notebooks_list:
    if notebook != 'readme.ipynb' and notebook.endswith('.ipynb'):
        notebooks.append(f"{notebooks_dir}/{notebook.replace('.ipynb', '')}")

notebooks = sorted(notebooks)

with open('index.rst', 'w') as file:
    file.write("""
.. include:: {notebooks_dir}/readme.rst

Navigation
^^^^^^^^^^

.. toctree::
   :maxdepth: 2
   :name: mastertoc

   {notebooks}


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

    """.format(notebooks='\n   '.join(notebooks), notebooks_dir=notebooks_dir))

os.system("jupyter nbconvert --to rst notebooks/readme.ipynb")
os.system("jupyter nbconvert --to markdown notebooks/readme.ipynb")
os.system("mv notebooks/readme.md ../../README.md")
