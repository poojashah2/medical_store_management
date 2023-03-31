from odoo import fields,models,api,_
from odoo.exceptions import ValidationError

class SymptomsInfo(models.Model):
	_name = 'symptoms.info'

	name = fields.Char(string="Symptoms name")
	medicine_ids = fields.One2many('medicine.info','symptom_id',string="Medicine name")

	