resumen-credicoop
=================

Aplicación para manipular la información del resumen del Banco credicoop.

La aplicación funciona desde consola y también como libreria.


Desde consola
-------------
```
python resumen-credicoop.py -f resumen.pdf
~$ python resumen-credicoop.py -h
usage: resumen-credicoop.py -f <filename> [--fazio]
```

Filename es el PDF que se descarga desde el home banking del banco credicoop.

La opción --fazio, es util para las cooperativas que llevan la contabilidad con ... Carlos Fazio, ya que genera
la planilla de calculos que hay que pasarle.

Si no se pasa esta opción, el sistema solo imprime el resumen en pantalla.


Como librería
-------------


```PYTHON
>>> from credicoop.process import ParseCredicoop
>>> filename = "resumen.pdf"
>>> credicoop = ParseCredicoop(filename)
>>> obj = credicoop.create()
```

Todo el resumen

```PYTHON
>>> obj.to_dict()

```

```JSON
{

    'saldo':'xxxx.xx',
    'saldo_anterior':'xxxx.xx',
    'fecha_saldo':'dd/mm/yy'
    'detalle':[
        {
            'fecha':u'dd/mm/yy',
            'credito':u'xxx',
            'comprobante':u'xxx',
            'saldo':u'xxx',
            'descripcion':u'descripcion',
            'debito':u'xxx'
        },
        {
            'fecha':u'dd/mm/yy',
            'credito':u'xxx',
            'comprobante':u'xxx',
            'saldo':u'xxx',
            'descripcion':u'descripcion',
            'debito':u'xxx'
        }
        ],
    }

```

Obtener la información

```PYTHON
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
```
