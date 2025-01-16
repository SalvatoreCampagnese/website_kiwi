{
   'name': 'Kiwi Theme',
   'description': 'Kiwi Trade Platform Theme',
   'category': 'Theme',
   'version': '1.0.1',
   'author': 'Nebula S.r.l',
   'license': 'AGPL-3',
   'depends': ['website'],
   'data': [],
   'assets': {
      'web._assets_primary_variables': [
         ('prepend', 'website_kiwi/static/src/scss/primary_variables.scss'),
      ],
      'web.assets_frontend': [
         'website_kiwi/static/src/scss/font.scss',
      ],
   },
}