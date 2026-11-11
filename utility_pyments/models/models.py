# from odoo import models, fields, api


# class utility_pyments(models.Model):
#     _name = 'utility_pyments.utility_pyments'
#     _description = 'utility_pyments.utility_pyments'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

