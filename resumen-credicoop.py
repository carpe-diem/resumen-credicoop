#!/usr/bin/python
# -*- coding: utf-8 -*-

import getopt
import sys

from credicoop.process import ParseCredicoop
from credicoop.constants import TITLE, TITLE_PREV, TITLE_LAST


HELP = """python credicoop.py -f <filename>"""


def main(argv):
    filename = ''

    try:
        opts, args = getopt.getopt(argv,"h:f:",["filename="])

    except getopt.GetoptError:
        print HELP
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print HELP
            sys.exit()
        elif opt in ("-f", "--file"):
            filename = arg

    if not filename:
        print HELP

    else:
        try:
            credicoop = ParseCredicoop(filename)
            obj = credicoop.create()

            print u"{0}{1}\n".format(
                TITLE_PREV.rjust(20), obj.saldo_anterior.rjust(30))

            print u"{0}{1}{2}{3}{4}{5}".format(
                    TITLE[0].rjust(0),
                    TITLE[1].rjust(20),
                    TITLE[2].rjust(30),
                    TITLE[3].rjust(20),
                    TITLE[4].rjust(15),
                    TITLE[5].rjust(10))

            for x in obj.items:
                "{}".rjust(4)
                print u"{0}{1}{2}{3}{4}{5}".format(
                    x.fecha.rjust(10),
                    x.comprobante.rjust(10),
                    x.descripcion.rjust(40),
                    x.debito.rjust(15),
                    x.credito.rjust(15),
                    x.saldo.rjust(15))

            print u"\n{0}{1}{2}".format(TITLE_LAST.rjust(20), obj.fecha_saldo.rjust(10),
                    obj.saldo.rjust(20))

        except Exception, e:
            print e


if __name__ == "__main__":
   main(sys.argv[1:])

