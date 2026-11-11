from odoo import models, fields, api


class UTAppartment(models.Model):
    _name = 'ut.apartment'
    _description = 'Apartment'

    #res.partner
    #product.product

    name = fields.Char(
        string='Name',
    )
    address = fields.Char(
        string='Address',
    )

