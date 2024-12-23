# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Encyclopedia 3.A'
copyright = '2025, Vincent Deguin'
author = 'Vincent Deguin'
release = '0.0.1'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

comments_config = {
   "utterances": {
      "repo": "https://github.com/Deugz/Encyclopedia-Home",
      "optional": "config",
   }
}

comments_config = {
   "hypothesis": True
}



extensions = [
  
  "myst_parser",
  "sphinx_design",
  "sphinx_comments",
  "sphinx_new_tab_link",
  "sphinx_book_theme",
  "sphinx_togglebutton",
  "sphinx_thebe",
]

myst_enable_extensions = ["colon_fence", "linkify", "substitution"]
myst_heading_anchors = 2



templates_path = ['_templates']
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_logo = "_static/Logo/Encyclopedia-logo.png"
html_favicon = "_static/Logo/Encyclopedia-logo.png"
html_static_path = ['_static']

html_theme_options = {
    "analytics": {"google_analytics_id": "G-E1LZY6PF7T"},
    "external_links": [
        {
            "url": "https://deugz.github.io/sp-Science_Journey/build/html/index.html",
            "name": "&nbsp &nbsp &nbsp &nbsp 💫 Research",
            "attributes": {"target": "_blank"},
        },
        {
            "url": "https://deugz.github.io/sp-Education_Journey/build/html/index.html",
            "name": "&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp 🧠 Education",
            "attributes": {"target": "_blank"},
        },
        {
            "url": "https://deugz.github.io/sp-Hiphop_Journey/build/html/index.html",
            "name": "&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp 🎤 Culture ",
            "attributes": {"target": "_blank"},
        },
        {
            "url": "https://deugz.github.io/sp-Politique_Journey/build/html/index.html",
            "name": " &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp ✊ Société",
            "attributes": {"target": "_blank"},
        },
    ],
    "header_links_before_dropdown": 11,    
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/Deugz/Encyclopedia-Home",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "Bullet Journal",
            "url": "https://deugz.github.io/jb-bullet-2025/_build/html/intro.html",
            "icon": "fa-solid fa-compass",
        },
        {
            "name": "Tools",
            "url": "https://deugz.github.io/nb-tools/_build/html/intro.html",
            "icon": "fa-solid fa-screwdriver-wrench",
        },
        {
            "name": "Blog",
            "url": "https://deugz.github.io/ab-blog/_website/index.html",
            "icon": "fa-solid fa-blog",
        },
    ],   

    "logo": {
        "text": " &nbsp Viny 3.A &nbsp ",
        "image_dark": "_static/Logo/Encyclopedia-logo.png",
        "alt_text": " &nbsp V. Deguin &nbsp &nbsp",
    },
    
    
    "navbar_start": ["navbar-logo"],
    
}


html_css_files = ["css/custom_style.css", "css/Cube.css", "css/coffee_cup.css", "css/kittons.css", "css/style_book_shell.css", "css/style_flipping_card.css", "css/style_wheel.css", "css/periodic-table.css", "css/style-dialogue.css", "css/cell-aggregation.css", "css/style-bird.css", "css/slider.css",'https://fonts.googleapis.com/css2?family=Fredoka:wght@400;700&family=Montserrat:wght@400;700&display=swap']
html_js_files = ["assets/script/kittons.js", "assets/script/script_flipping_card.js", "assets/script/script_wheel.js", "assets/script/scriptvideo.js", "assets/script/cell-aggregation.js", "assets/script/slider-script.js"]

    
