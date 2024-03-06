# -*- coding: utf-8 -*-
# from odoo import http


# class CustomProductInventory(http.Controller):
#     @http.route('/custom_product_inventory/custom_product_inventory', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_product_inventory/custom_product_inventory/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_product_inventory.listing', {
#             'root': '/custom_product_inventory/custom_product_inventory',
#             'objects': http.request.env['custom_product_inventory.custom_product_inventory'].search([]),
#         })

#     @http.route('/custom_product_inventory/custom_product_inventory/objects/<model("custom_product_inventory.custom_product_inventory"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_product_inventory.object', {
#             'object': obj
#         })

