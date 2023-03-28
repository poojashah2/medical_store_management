from odoo import models,fields,api,_

class SymptomsMedicineInfo(models.Model):
	_name = 'symptoms.medicine.info'

	medicine_ids = fields.Many2many('medicine.info',string="Medicine name")
	symptoms_id = fields.Many2one('symptoms.info',string="Symptoms name")