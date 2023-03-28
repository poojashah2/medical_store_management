from odoo import fields,models,api,_

class SymptomsInfo(models.Model):
	_name = 'symptoms.info'

	name = fields.Char(string="Symptoms name")