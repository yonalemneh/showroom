# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class showroom_showroom(models.Model):
    _name = 'showroom.showroom'
    _description = 'Showroom'

    showroom = fields.Char("Showroom", required=True)
    showroom_contact = fields.Char("Contact Phone")

    _rec_name = 'showroom'

class SaleOrder(models.Model):
    _inherit = "sale.order"

    showroom_id = fields.Many2one('showroom.showroom' , 'Showroom')

    # @api.onchange('showroom_name')
    # def onchange_showroom_name(self):
    #     if self.showroom_name:
    #         self.showroom_contact_id = self.showroom_name.uom_id.id
    #
    #
    # def _prepare_showroom_values(self):
    #     self.ensure_one()
    #     return {
    #         'showroom_name': self.showroom_name.id ,
    #         'showroom_contact': self.showroom_contact_id.id ,
    #     }
