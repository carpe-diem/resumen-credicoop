# -*- coding: utf-8 -*-
from cStringIO import StringIO
from lxml import etree

from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import HTMLConverter
from pdfminer.layout import LAParams

from credicoop.resume import Resumen, ResumenDetalle
from credicoop.constants import CODEC, TITLE, TITLE_PREV, TITLE_LAST


class ParseCredicoop(object):

    def __init__ (self, filename):
        self.filename = filename
        self.content = self.get_content()

    def get_content(self):
        doc = self.convert_pdf()
        tree = etree.HTML(doc)
        content = tree.xpath("/html/body/div[6]//text()")

        new_line = []
        for x in content:
            line = x.strip()
            if line:
                new_line.append(line)

        return new_line

    def convert_pdf(self):

        rsrcmgr = PDFResourceManager()
        retstr = StringIO()
        codec = CODEC
        laparams = LAParams()
        device = HTMLConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)

        fp = file(self.filename, 'rb')
        process_pdf(rsrcmgr, device, fp)
        fp.close()
        device.close()

        str = retstr.getvalue()
        retstr.close()
        return str


    def create(self):
        resumen = Resumen()

        for line in self.content:

            if all([x in TITLE for x in line.split()]):
                continue

            if TITLE_PREV in line:
                saldo_anterior = line.strip().strip(TITLE_PREV)
                saldo_anterior = saldo_anterior.replace('.', '')
                saldo_anterior = saldo_anterior.replace(',', '.')
                resumen.saldo_anterior = saldo_anterior

            elif TITLE_LAST in line:
                fecha, saldo = line.strip().strip(TITLE_LAST).split()
                saldo = saldo.replace('.', '')
                saldo = saldo.replace(',', '.')
                resumen.saldo = saldo
                resumen.fecha_saldo = fecha

            else:
                detalle = ResumenDetalle()

                detalle.fecha = line[0:8]
                detalle.comprobante = line[9:21].strip()
                detalle.descripcion = line[21:50].strip()
                detalle.debito = line[50:64].strip()
                detalle.credito = line[64:98].strip()
                detalle.saldo = line[85:].strip()

                resumen.items.append(detalle)

        return resumen

