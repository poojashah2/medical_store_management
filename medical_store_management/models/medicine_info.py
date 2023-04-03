from odoo import models,fields,api,_
from datetime import date, datetime
from odoo.exceptions import ValidationError
import calendar

class MedicineInfo(models.Model):
    _name = 'medicine.info'

    name = fields.Char(string="Medicine name")
    reference_number = fields.Char(string="Reference Number",readonly=True,copy=False)
    is_major = fields.Boolean(string="is major")
    company_name = fields.Char(string="Company name")
    dosage_form = fields.Selection([('tablet','Tablet'),('capsule','Capsule'),('liquid','Liquid')],string="Dosage form")
    symptoms_count = fields.Integer(string="Symptoms count")

    @api.model
    def default_get(self,fields):
        res = super(MedicineInfo,self).default_get(fields)
        if 'company_name' in fields:
            res['company_name'] = "icreative"
        return res

    @api.model
    def create(self, vals):
        print('---------',self)
        print('---------',vals)
        print('-----',vals.get('reference_number'))
        # date_today = datetime.now().date().strftime("%Y-%m-%d")
        # medicine_rec = self.env['medicine.info'].search([('expiry_date','>',date_today)])
        # print('--->>----',medicine_rec)
        # for rec in medicine_rec:
        #     print('bvcvc',rec.name)
        if not vals.get('reference_number'):
            print("\n\n\n\n", self.env["ir.sequence"])
            seq = self.env["ir.sequence"].next_by_code('pooja.shah')
            print("seq>>>>>>>>>>>>>>>>>>>>>>>",seq)
            month = calendar.month_name[date.today().month]
            print("month>>>>>",month)
            vals['reference_number'] = seq[0:3]+'/'+month[0:3]+'/'+seq[3:]
            print(vals['reference_number'])
        return super(MedicineInfo,self).create(vals)

    # def action_medicine_detail(self):
    #     action = {
    #         "type": "ir.actions.act_window",
    #         "res_model": "medicine.info",
    #         "name": _("Medicine"),
    #         'view_mode': 'tree'
    #     }
    #     return action


    # def action_symptoms_count(self):
    #     model_rec = self.env['medicine.symptoms.info'].search_count([('symptoms_ids', '=', 14)])
    #     print("\n\n\n\n reccccccc", model_rec)
    #     self.symptoms_count = model_rec
    #     return self.symptoms_count