{
    'name' : 'medical store',
    'version' : '15.0.0.1.0',
    'description' : 'Medical store module details',
    'depends' : [],
    'data' : [
        'security/ir.model.access.csv',
        'views/medicine_info.xml',
        'views/symptoms_info.xml',
        'views/stock_info.xml',
    ],
    'installable' : True,
    'application' : True,
    'auto_install' : False,
}