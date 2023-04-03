from odoo import models,fields,api
from datetime import date,datetime

class MedicineSymptomsInfo(models.Model):
	_name = 'medicine.symptoms.info'
	date_today = datetime.now().date().strftime("%Y-%m-%d")


	medicine_id = fields.Many2one('medicine.info',string="Medicine name")
	symptoms_ids = fields.Many2many('symptoms.info', 'symptoms_id', string="Symptoms name")