{
    'name' : 'medical store',
    'version' : '15.0.0.1.0',
    'description' : 'Medical store module details',
    'depends' : [],
    'data' : [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/medicine_info.xml',
        'views/symptoms_info.xml',
        'views/stock_info.xml',
        'views/medicine_symptoms_info.xml',
    ],
    'installable' : True,
    'application' : True,
    'auto_install' : False,
}