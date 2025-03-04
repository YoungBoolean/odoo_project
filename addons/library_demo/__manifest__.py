# -*- coding: utf-8 -*-
{
    'name': "Library",

    'summary': """
        Library module""",

    'description': """
        Library Management System
    """,

    'author': "Paulius Uvarovas",
    'website': "https://github.com/YoungBoolean",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/email_template.xml',
        'data/cron_jobs.xml',
        'views/library_book_views.xml',
        'views/library_book_menus.xml',
        'views/library_book_issue_views.xml',
        'views/library_book_issue_menus.xml',
        'views/library_book_registration_form_views.xml',
        'views/library_book_registration_form_menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
