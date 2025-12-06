from odoo import models,api,fields,_
from odoo.exceptions import ValidationError

class HrAttendance(models.Model):
    _inherit = 'hr.attendance'

    @api.constrains('employee_id','check_in','check_out')

    def _check_duplicate(self):

        for rec in self:
            if rec . check_out:
                continue


            checkin_datetime=fields.Datetime.context_timestamp(rec,rec.check_in)
            checkin_date_start=checkin_datetime.replace(hour=0,minute=0,second=0)
            checkin_date_end=checkin_datetime.replace(hour=23,minute=59,second=59)


            domain=[

                    ('id','!=',rec.id),
                    ('employee_id','=',rec.employee_id.id),
                ('check_out', '=', False),
                    ('check_in','>=',fields.Datetime.to_string(checkin_date_start)),
                    ('check_in','<=',fields.Datetime.to_string(checkin_date_end))

            ]

            if self.search_count(domain):
                    raise ValidationError(_( 'employee already has an active attendance for this date.'))