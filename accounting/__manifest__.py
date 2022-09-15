# -*- coding: utf-8 -*-
{
    'name': "Full Features Accounting App",
    'summary': """
        Full Features Accounting App""",

    'description': """
        Adding Administrator rights to access rights in users screen
        Open the hidden full accounting features for users with administrator rights
        Renaming the invoicing app to accounting
        Renaming the invoicing app in settings to accounting
        Ability to translate Journals
        Ability to translate COA names
    """,
    'author': "Odoo Pro 365",
    'website': "https://odoopro365.com",
    "support": "maherkhalil@outlook.com",
    "license": "OPL-1",
    'category': 'Accounting/Accounting',
    'version': '15.0.1',
    'depends': ['base', 'account'],
    'data': [
        # 'security/ir.model.access.csv',
        'security/accounting_security.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    "images": ["static/description/background.png", ],
    "training_video": "",
    'application': True,
    "auto_install": False,
    "installable": True,
    "price": 20,
    "currency": "EUR",

}
