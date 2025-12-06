from odoo import models, fields, api
from odoo.exceptions import ValidationError


class HrAttendance(models.Model):
    _inherit = 'hr.attendance'

    @api.constrains('check_in', 'check_out', 'employee_id')
    def _check_duplicate_attendance(self):
        for record in self:
            if not record.check_out:
                # Search for other open attendances for the same employee on the same day
                domain = [
                    ('employee_id', '=', record.employee_id.id),
                    ('check_out', '=', False),
                    ('id', '!=', record.id),
                    ('check_in', '>=', fields.Datetime.to_string(
                        fields.Datetime.context_timestamp(record, record.check_in).replace(hour=0, minute=0, second=0)
                    )),
                    ('check_in', '<', fields.Datetime.to_string(
                        fields.Datetime.context_timestamp(record, record.check_in).replace(hour=23, minute=59,
                                                                                           second=59)
                    ))
                ]

                duplicate = self.search(domain, limit=1)
                if duplicate:
                    raise ValidationError(
                        "Employee already has an active attendance for this date."
                    )