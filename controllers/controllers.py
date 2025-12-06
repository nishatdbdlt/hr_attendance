# -*- coding: utf-8 -*-
# from odoo import http


# class HrAttendance(http.Controller):
#     @http.route('/hr__attendance/hr__attendance', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr__attendance/hr__attendance/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr__attendance.listing', {
#             'root': '/hr__attendance/hr__attendance',
#             'objects': http.request.env['hr__attendance.hr__attendance'].search([]),
#         })

#     @http.route('/hr__attendance/hr__attendance/objects/<model("hr__attendance.hr__attendance"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr__attendance.object', {
#             'object': obj
#         })

