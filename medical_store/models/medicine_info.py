from odoo import models,fields,api,_
from datetime import date, datetime
from odoo.exceptions import ValidationError
import calendar

class MedicineInfo(models.Model):
    _name = 'medicine.info'

    name = fields.Char(string="Medicine name")
    reference_number = fields.Char(string="Reference Number",readonly=True,copy=False)
    manufacturing_date = fields.Date(string="Manufacturing Date")
    is_major = fields.Boolean(string="is major")
    expiry_date = fields.Date(string="Expiry Date")
    # symptom_ids = fields.Many2many('symptoms.info',string="Symptoms")
    dosage_form = fields.Selection([('tablet','Tablet'),('capsule','Capsule'),('liquid','Liquid')],string="Dosage form")
    # remaining_months = fields.Char(string="Remaining Months", compute="compute_remaining_months")
    
    # def compute_remaining_months(self):
    #     current_day = date.today()
    #     month_difference = 0
    #     for rec in self:
    #         if rec.manufacturing_date:
    #             month_difference = (current_day.year - rec.manufacturing_date.year) * 12 + (current_day.month - rec.manufacturing_date.month)
    #             if rec.expiry_month > month_difference:
    #                 rec.remaining_months = rec.expiry_month - month_difference
    #             else:
    #                 rec.remaining_months = "Expired"
    #         else:
    #             rec.remaining_months = 0



    def action_medicine_detail(self):
        # model_ref = self.env["symptoms.info"].search(['medicine_ids','=',self.id])
        # print(model_ref)
        # for rec in model_ref:
        #     print(rec.manufacturer)
        action = {
            "type": "ir.actions.act_window",
            "res_model": "medicine.info",
            "name": _("Medicine"),
            'view_mode': 'tree'
        }
        return action



    @api.model
    def create(self, vals):
        print('---------',self)
        print('---------',vals)
        print('-----',vals.get('reference_number'))
        date_today = datetime.now().date().strftime("%Y-%m-%d")
        medicine_rec = self.env['medicine.info'].search([('expiry_date','>',date_today)])
        print('--->>----',medicine_rec)
        for rec in medicine_rec:
            print('bvcvc',rec.name)
        if not vals.get('reference_number'):
            print("\n\n\n\n", self.env["ir.sequence"])
            seq = self.env["ir.sequence"].next_by_code('pooja.shah')
            print("seq>>>>>>>>>>>>>>>>>>>>>>>",seq)
            month = calendar.month_name[date.today().month]
            print("month>>>>>",month)
            vals['reference_number'] = seq[0:3]+'/'+month[0:3]+'/'+seq[3:]
            print(vals['reference_number'])
        return super(MedicineInfo,self).create(vals)

    def write(self,vals):
        date_ex = vals.get('expiry_date')
        today_date = datetime.now().date().strftime("%Y-%m-%d")
        if not date_ex:
            raise ValidationError('please fill the expiry_date field')
        else:
            if today_date > date_ex:
                raise ValidationError('your medicine is expired')
        return super(MedicineInfo,self).write(vals)

        # MED0001