from odoo import fields, models


class UTApartment(models.Model):
    _name = 'up.apartment'
    _description = 'Apartment'

    name = fields.Char(
        string='Name',
        required=True,
    )
    address = fields.Char(
        string='Address',
        required=True,
    )

    apartment_utility_ids = fields.One2many(
        string='Apartment Utility list',
        comodel_name='up.apartment.utility',
        inverse_name='apartment_id',
    )