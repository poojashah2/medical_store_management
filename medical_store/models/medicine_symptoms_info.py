from odoo import models,fields,api

class MedicineSymptomsInfo(models.Model):
	_name = 'medicine.symptoms.info'

	medicine_id = fields.Many2one('medicine.info',string="Medicine name")
	symptoms_ids = fields.Many2many('symptoms.info',string="Symptoms name")