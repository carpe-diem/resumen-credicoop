resumen-credicoop
=================

Resumen del Banco credicoop


python resumen-credicoop.py -f resumen.pdf



>>> from src.process import ParseCredicoop
>>> filename = "resumen.pdf"
>>> credicoop = ParseCredicoop(filename)
>>> obj = credicoop.create()
>>> obj.saldo_anterior
'26797.47'
>>> obj.saldo
'10819.91'
>>> obj.fecha_saldo
'28/02/13'
>>> obj.items[0].fecha
u'30/01/13'
>>> obj.items[0].descripcion
u'IMP. L.25413\u2212DEB Y/O CRED'
>>> obj.items[0].debito
u'1,17'
>>> obj.items[2].descripcion
'IVA DEBITO FISCAL 21%'
>>> obj.items[3].descripcion
'CHEQUE PAGADO POR CAJA'
>>> obj.items[5].descripcion
'TRANSF.AUTOM.GRAV.CRE/DEB'
>>> obj.items[5].credito
''
>>> obj.items[5].debito
'6.000,00'
