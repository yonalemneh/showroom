# -*- coding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#    46 4c 4f 57 43 4f 44 45
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
#    This module is developed by Flowcode Technology Solutions for GM Furniture
#    http://www.flow-code.net
#    (C) Flowcode Technology Solutions - 2018
##############################################################################

{
    'name': 'Showroom',
    'author': 'Flowcode Technology Solutions',
    'category': 'Sales Management',
    'website': 'http://www.flow-code.net',
    'description': """Manage Shop For Every Sales Order - Git""",
    'version': '10.0.1',
    'depends': ['sale'],
    'data': [
            'views/showroom_view.xml',
            'report/showroom_report_templates.xml',
            'report/report_showroom.xml'
            ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
