# -*- coding: utf-8 -*-
{
    'name': "openacademy",

    'summary': "The Academy",

    'description': "This is the openacademy system",

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','board'],

    # always loaded
    'data': [
        "security/security.xml",
        "security/ir.model.access.csv",
        'views/openacademy.xml',
        'views/partner.xml',
        #'views/session_board.xml',
        'wizard/add_attendes_wizard.xml',
        'reports/session_report.xml',
        'reports/course_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
