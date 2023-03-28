from odoo import models,fields,api,_

class MedicineInfo(models.Model):
    _name = 'medicine.info'

    name = fields.Char(string="Medicine name")
    reference_number = fields.Char(string="Reference Number")
    manufacturer = fields.Char(string="Manufacturer")
    is_major = fields.Boolean(string="is major")
    expiry_month = fields.Date(string="Expiry date")
    dosage_form = fields.Selection([('tablet','Tablet'),('capsule','Capsule'),('liquid','Liquid')],string="Dosage form")


    def action_symptoms_detail(self):
        action = {
            "type": "ir.actions.act_window",
            "res_model": "symptoms.info",
            "name": _("Medicine"),
            'view_mode': 'tree,form'
        }
        return action