from odoo import models,fields,api,_

class StockInfo(models.Model):
	_name = 'stock.info'

	medicine_name_id = fields.Many2one('medicine.info',string="Medicine name")
	sold_quantity = fields.Integer(string="Sold Quantity")
	total_quantity = fields.Integer(string="Total Quantity")
	available_quantity = fields.Integer(string="Available Quantity",compute="_compute_quantity_status")

	def _compute_quantity_status(self):
		for rec in self:
			rec.available_quantity = rec.total_quantity - rec.sold_quantity
	

