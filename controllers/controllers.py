# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class Openacademy(http.Controller):
    @http.route('/openacademy/sessions/',auth='user', website=True )

    def index(self, **kw):
        sessions=http.request.env['openacademy.session'].sudo().search([])

        return request.render("openacademy.openacademy_session", {'sessions':sessions})

    # function that get information from api
    @http.route('/get_sessions',type="json", auth='user', website=True)
    def get_sessions(self):
        print(" yes here entered ")
        sessions_rec = http.request.env['openacademy.session'].search([])
        sessions=[]
        for rec in sessions_rec:
            vals = {
                "id" : rec.id,
                "name" : rec.name,
                "belong to": rec.course_id.name
            }
            sessions.append(vals)
        data={"status":200,"response":sessions,"message":"SUCCESS"}
        return data

    # function that create and add information to module from app
    @http.route('/create_sessions', type="json", auth='user', website=True)
    def create_sessions(self,**rec):
        print("rec",rec)
        if rec['name'] and rec["course_id"]:
            vals={
                "name":rec['name'],
                "seats":rec['seats'],
                "course_id":rec["course_id"]
            }
            sessions_new = http.request.env['openacademy.session'].create([vals])
            print(sessions_new)
            data = {"success":True,"message": "session created","id":sessions_new.id}
        return data

    # function that update and add information to module from app
    @http.route('/update_sessions', type="json", auth='user', website=True)
    def update_sessions(self, **rec):
        print("rec", rec)
        if rec['id']:
            sessions_id = http.request.env['openacademy.session'].search([("id","=",rec["id"])])
            if sessions_id:
                sessions_id.write(rec)
            data = {"success": True, "message": "session updated"}
        return data

    # function that delete from module
    @http.route('/delete_sessions', type="json", auth='user', website=True)
    def delete_sessions(self,id):
        print("id removed", id)

        sessions_removed = http.request.env['openacademy.session'].search([("id","=",id)])
        sessions_removed.unlink()
        print(sessions_removed)
        data = {"success": True, "message": "session deleted", "id": sessions_removed.id}
        return data


    # def index_1(self, **kw):
    #     courses = http.request.env['openacademy.course'].sudo().search([])
    #
    #     return request.render("openacademy.openacademy_course", {'courses': courses})

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
