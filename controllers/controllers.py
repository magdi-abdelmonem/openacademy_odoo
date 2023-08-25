# -*- coding: utf-8 -*-
from odoo import http


class Openacademy(http.Controller):
    @http.route('/openacademy/openacademy', auth='public')

    def index(self, **kw):
        filter_course=http.request.env['openacademy.session'].search([])
        output="<h1>Openacademy Sessions</h1><ul>"
        for rec in filter_course:
            output+='<li>' + rec['name'] + '</li>'
            print(output)
        output+='</ul>'
        return output

    # @http.route('/openacademy/openacademy/objects', auth='public')
    # def list(self, **kw):
    #     return http.request.render('openacademy.listing', {
    #         'root': '/openacademy/openacademy',
    #         'objects': http.request.env['openacademy.course'].search([]),
    #     })

#     @http.route('/openacademy/openacademy/objects/<model("openacademy.openacademy"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openacademy.object', {
#             'object': obj
#         })
