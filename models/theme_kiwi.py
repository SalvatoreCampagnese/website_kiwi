from odoo import fields, models, _

class TestModel(models.Model):
    _name = "kiwi_test_model"
    
    name = fields.Char('Description', required=True, translate=True)