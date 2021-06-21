# -*- coding: utf-8 -*-

from odoo import models, fields, api


class school_management(models.Model):
    _name = 'school.management.teacher'
    _description = 'Teacher Table'

    name = fields.Char( sring="Name",required=True)
    age = fields.Integer(string="Age")
    guardian = fields.Char(sring="Guardian")
    note = fields.Text(string="Notes")
    gender=fields.Selection([
        ('male', 'male'),
        ('female','female'),
        ('other','other')
    ], string='Gender',deafult='male')
    image=fields.Binary(string='Image')
