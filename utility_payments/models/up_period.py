from dateutil.relativedelta import relativedelta

from odoo import fields, models, api
from odoo.tools import date_utils


class UPApartmentUtility(models.Model):
    _name = 'up.period'
    _description = 'List of periods (months) for which accruals and payments are recorded'

    name = fields.Char(
        readonly=True,
        store=True,
        compute='_compute_name',
    )
    date = fields.Date(
        string='Date',
        readonly=True,
        required=True,
    )

    sql_constraints = [
        ('uniq_period_date', 'unique(date)',
         'Період з такою датою вже існує!'),
    ]

    @api.depends('date')
    def _compute_name(self):
        """Generates a name based on the date"""
        # for rec in self:
        #     rec.name = rec.date.strftime('%b %Y')

        months = ['Січень', 'Лютий', 'Березень', 'Квітень', 'Травень',
                  'Червень', 'Липень', 'Серпень', 'Вересень', 'Жовтень',
                  'Листопад', 'Грудень']
        for rec in self:
            if rec.date:
                rec.name = f"{months[rec.date.month - 1]} {rec.date.year}"
            else:
                rec.name = False

    def action_open_generate_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'up.period.generate.wizard',
            'view_mode': 'form',
            'target': 'current',
        }

    @api.model
    def _month_start(self, any_date):
        """Перший день місяця для довільної дати."""
        return fields.Date.to_date(any_date).replace(day=1)

    @api.model
    def _get_or_create(self, any_date):
        """Find or Create period for any_day"""
        start = self._month_start(any_date)
        period = self.search([('date', '=', start)], limit=1)
        if not period:
            period = self.create({'date': start})
        return period

    @api.model
    def _ensure_range(self, date_from, date_to):
        """Створити всі пропущені періоди в інтервалі [date_from; date_to].
        Повертає записи, що були створені."""
        start = self._month_start(date_from)
        end = self._month_start(date_to)
        if start > end:
            start, end = end, start
        existing = set(self.search([
            ('date', '>=', start),
            ('date', '<=', end),
        ]).mapped('date'))
        new_periods = self.browse()
        current = start
        while current <= end:
            if current not in existing:
                new_periods |= self.create({'date': current})
            current += relativedelta(months=1)
        return new_periods
