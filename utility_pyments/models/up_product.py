from odoo import models, fields, api


class UPProductProduct(models.Model):
    _name = 'product.product'
    _inherit = ['product.product']

    personal_account=fields.Char(
        string='Personal Account',
        )

    provider   =fields.Many2one(
        string='Provider',
        comodel_name='res.partner',
    )