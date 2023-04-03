from odoo import models,fields,api,_
from datetime import datetime,date

class MedicineLotInfo(models.Model):
	_name = 'medicine.lot.info'

	lot = fields.Char(string="Medicine lot no",readonly=True,copy=False)
	medicine_name_id = fields.Many2one('medicine.info',string="Medicine name")
	manufacture_date = fields.Date(string="Manufacturing Date")
	expiry_date = fields.Date(string="Expiry Date")
	lot_quantity = fields.Integer(string="lot Quantity")
	state_lot = fields.Selection(selection=[('draft', 'Expired'),('done', 'Not Expired')], string='Status', required=True, readonly=True, copy=False, tracking=True, default='draft')



	@api.model
	def create(self, vals):
	    print('---------',self)
	    print('---------',vals)
	    print('-----',vals.get('lot'))
	    if not vals.get('lot'):
	        # print("\n\n\n\n", self.env["ir.sequence"])
	        seq = self.env["ir.sequence"].next_by_code('medicine.lot')
	        print("seq>>>>>>>>>>>>>>>>>>>>>>>",seq)
	        # print("month>>>>>",month)
	        vals['lot'] = seq
	        print(vals['lot'])
	    return super(MedicineLotInfo,self).create(vals)