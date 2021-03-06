resumen-credicoop
=================

Aplicación para manipular la información del resumen del Banco Credicoop.

La aplicación funciona desde consola y también como librería.


Instalación
-----------

```
~$ pip install resumen-credicoop
```

Nota:
~~~~
En ubuntu/debian quizas necesiten instalar otros paquetes por lxml.

```
sudo apt-get install libxml2-dev
sudo apt-get install libxslt1-dev
```

Desde consola
-------------

```
~$ resumen-credicoop -h
usage: resumen-credicoop -f <filename> [--fazio]
```

Filename es el PDF que se descarga desde el home banking del banco Credicoop.

La opción --fazio, es útil para las cooperativas que llevan la contabilidad con ... Carlos Fazio, ya que genera
la planilla de cálculos que hay que pasarle.

```
~$ resumen-credicoop -f resumen.pdf --fazio
```

Si no se pasa esta opción, el sistema solo imprime el resumen en pantalla.


```
~$ resumen-credicoop -f resumen.pdf
```


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
    'fecha_saldo':'dd/mm/yy',
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
    ]
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
