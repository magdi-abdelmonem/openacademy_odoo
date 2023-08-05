# -*- coding: utf-8 -*-
from odoo import models, fields, api,_
from odoo.exceptions import ValidationError
from datetime import timedelta

class Course (models.Model):
    _name = 'openacademy.course'
    _description = 'OpenAcademy Course'

    name = fields.Char(string="title",required=True)
    description = fields.Text()
    responsible_id=fields.Many2one("res.users",Ondelete="set null",string="Responsible",Index=True)
    session_id=fields.One2many("openacademy.session","course_id",string="Sessions")

    _sql_constraints = [
        ('name_description_check',
         'CHECK(name!= description)',
         "the title of course should not be the title of description"),

        ('name_uniq', 'unique (name)', "Tag name already exists !")

    ]


class Sessions(models.Model):
    _name = 'openacademy.session'
    _description = 'OpenAcademy Sessions'

    name = fields.Char( required=True)
    start_date=fields.Date(default=fields.date.today())
    end_date=fields.Date(string="end data",store=True, compute= '_get_end_date', inverse='_set_end_date')
    color=fields.Integer()
    active=fields.Boolean(default=True)
    duration=fields.Float(digits=(2,6),help="duration in days")
    seats=fields.Integer(string="number of seats" , default=10)
    instructor_id = fields.Many2one("res.partner",string="Instructor")
    course_id = fields.Many2one("openacademy.course", Ondelete="cascade", string="Course", required=True)
    attendee_ids=fields.Many2many("res.partner",string="Attendes")
    taken_seats=fields.Float(string="Taken Seats",compute= '_taken_seats')
    attendees_count=fields.Integer(string="Attendees Count ",store=True, compute= '_get_attendees_count')


    @api.depends("start_date", "duration")
    def _get_end_date(self):
        for rec in self:
            if not(rec.start_date and rec.duration):
                rec.end_date=rec.start_date
                continue

            duration = timedelta(days=rec.duration, seconds=-1)
            rec.end_date = duration + rec.start_date

    def _set_end_date(self):
        for rec in self:
            if not(rec.start_date and rec.duration):
                rec.end_date=rec.start_date
                continue

            rec.duration=(rec.end_date-rec.start_date).days+1



    #compute seat percentage
    @api.depends("seats","attendee_ids")
    def _taken_seats(self):
        for rec in self:
            if not rec.seats:
                rec.taken_seats=0.0
            else:
                rec.taken_seats=100*(len(rec.attendee_ids)/rec.seats)

    #count attendees

    @api.depends("attendee_ids")
    def _get_attendees_count(self):
        for rec in self:
            rec.attendees_count = len(rec.attendee_ids)



    @api.onchange("seats","attendee_ids")
    def _check(self):
        if self.seats<=0 :
            return {
                'warning':{
                    'title':_('Incorrect seat value'),
                    'message': 'the number of availble seat may not be negative'
                },

            }
        if self.seats<len(self.attendee_ids) :
            return {
                'warning':{
                    'title':_('many attendee'),
                    'message': _('you should increase seats or remove some attendee')
                },

            }

    @api.constrains("instructor_id","attendee_ids")
    def _check_instructor(self):
        for rec in self:
            if rec.instructor_id in rec.attendee_ids:
                raise ValidationError(_("the instructor cannot be an attendee"))