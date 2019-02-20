# -*- coding: utf-8 -*-
{
    'name': 'Convert number to words',
    'version': '12.0',
    'author': "Fogits Solutions",
    'website': "https://www.fogits.com/",
    'license': 'AGPL-3',
    'description': """
        Convert invoice amount to text 
    """,
    'images': ['static/description/convert.jpg'],
    'category': 'Accounting',
     'depends': [
        'base',
        'account',
    ],
    'data': [
        'views/account_invoice_view.xml',
        'views/account_invoice_report.xml',
        'views/account_config_setting_view.xml',
    ]
}
