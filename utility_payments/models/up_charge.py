from odoo import fields, models


class UPCharge(models.Model):
    _name = 'up.charge'
    _description = 'Utility Charges'

    state = fields.Selection(
        string='Status',
        selection=[
            ('draft', 'Draft'),
            ('approved', 'Approved'),
        ],
        default='draft',
    )

    apartment_id = fields.Many2one(
        string='Apartment',
        comodel_name='up.apartment',
        required=True,
    )

    period_id = fields.Many2one(
        string='Period',
        comodel_name='up.period',
        required=True,
    )

    charge_line_ids = fields.One2many(
        comodel_name='up.charge.line',
        inverse_name='charge_id',
        string='Charge lines',
    )