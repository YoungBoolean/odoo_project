# -*- coding: utf-8 -*-
# from odoo import http


# class LibraryDemo(http.Controller):
#     @http.route('/library_demo/library_demo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/library_demo/library_demo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('library_demo.listing', {
#             'root': '/library_demo/library_demo',
#             'objects': http.request.env['library_demo.library_demo'].search([]),
#         })

#     @http.route('/library_demo/library_demo/objects/<model("library_demo.library_demo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('library_demo.object', {
#             'object': obj
#         })
