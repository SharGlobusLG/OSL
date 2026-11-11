from odoo import models, fields, api


class UPApartmentService(models.Model):
    _name = 'up.apartment.service'
    _description = 'List of Services of each Apartment'

    # res.partner
    # product.product

    name = fields.Char(
        string='Name',
    )
    address = fields.Char(
        string='Address',
    )