# -*- coding: utf-8 -*-
# Part of Corsma. See LICENSE file for full copyright and licensing details.

{
    'name': 'Web Routing',
    'summary': 'Web Routing',
    'sequence': '9100',
    'category': 'Hidden',
    'description': """
Proposes advanced routing options not available in web or base to keep
base modules simple.
""",
    'data': [
        'views/http_routing_template.xml',
        'views/res_lang_views.xml',
    ],
    'depends': ['web'],
    'license': 'LGPL-3',
}
