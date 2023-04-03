from odoo import fields,models,api,_
from odoo.exceptions import ValidationError

class SymptomsInfo(models.Model):
	_name = 'symptoms.info'

	name = fields.Char(string="Symptoms name")

	def action_medicine_info(self):
	    model_rec = self.env['medicine.info'].search_count([])
	    print('-------',model_rec)