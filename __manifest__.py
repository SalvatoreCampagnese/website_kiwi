{
    # Theme information
    'name': "Kiwi Theme",
    'description': "Kiwi Theme",
    'category': 'Theme',
    'version': '0.1',
    'depends': ['website'],
    
    # templates
    'data': [
        'views/snippets/options.xml',
        'views/snippets/s_kiwi_quickactions.xml',
        'views/snippets/s_kiwi_heroslider.xml',
        'views/snippets/s_kiwi_productslider.xml',
        'views/snippets/s_kiwi_pointsbanner.xml',
        'views/snippets/s_kiwi_infobox.xml',
         'views/snippets/s_kiwi_learninginfo.xml',
         'views/snippets/s_kiwi_bigbanner.xml',
         'views/snippets/s_kiwi_twocolumn.xml',
         'views/snippets/s_kiwi_premiumtiers.xml',
         'views/snippets/s_kiwi_bigcards.xml',

        'views/website_templates.xml',
        'views/login_templates.xml',
    ],
    
    'assets': {
      'web.assets_frontend': [
         'kiwi_theme/static/src/scss/_variables.scss',
         'kiwi_theme/static/src/scss/_bootstrap_override.scss',
         'kiwi_theme/static/src/scss/_typography.scss',
         'kiwi_theme/static/src/scss/_inputs.scss',
         'kiwi_theme/static/src/scss/_buttons.scss',
         
         'kiwi_theme/static/src/scss/login/login_override.scss',

         'kiwi_theme/static/src/scss/snippets/s_kiwi_quickactions.scss',
         'kiwi_theme/static/src/scss/snippets/s_kiwi_heroslider.scss',
         'kiwi_theme/static/src/scss/snippets/s_kiwi_productslider.scss',
         'kiwi_theme/static/src/scss/snippets/s_kiwi_pointsbanner.scss',
         'kiwi_theme/static/src/scss/snippets/s_kiwi_infobox.scss',
         'kiwi_theme/static/src/scss/snippets/s_kiwi_learninginfo.scss',
         'kiwi_theme/static/src/scss/snippets/s_kiwi_bigbanner.scss',
         'kiwi_theme/static/src/scss/snippets/s_kiwi_twocolumn.scss',
         'kiwi_theme/static/src/scss/snippets/s_kiwi_premiumtiers.scss',
         'kiwi_theme/static/src/scss/snippets/s_kiwi_bigcards.scss',
         
         'kiwi_theme/static/src/img/wbuilder/s_kiwi_snippet.svg',
         '/kiwi_theme/static/src/img/pointsbanner/coins.png'
         'kiwi_theme/static/src/img/login.png',
         'kiwi_theme/static/src/img/logo.svg',
         'kiwi_theme/static/src/img/premiumtiers/check.svg',

         'kiwi_theme/static/src/js/hide.js',
      ],
      'web.assets_backend': [
         'kiwi_theme/static/src/js/hide.js',
      ]
   },

    # Your information
    'author': "Nebula S.r.l",
    'website': "https://www.explorenebula.com",
}
