#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):

        self.dicci_atributos = {"root-layout": ["width",
                                                "height", "background-color"],
                                "region": ["id", "top", "bottom",
                                           "left", "right"],
                                "img": ["src", "region", "begin",
                                        "dur"],
                                "audio": ["src", "begin", "dur"],
                                "textstream": ["src", "region"]}

        self.lista_etiquetas = []

    def startElement(self, etiqueta, attrs):

        self.diccionario_atributos = {}
        if etiqueta in self.dicci_atributos:
            self.diccionario_atributos["Etiqueta"] = etiqueta
            for atrib in self.dicci_atributos[etiqueta]:
                self.diccionario_atributos[atrib] = attrs.get(atrib, "")
            self.lista_etiquetas.append(self.diccionario_atributos)

    def get_tags(self):

        return (self.lista_etiquetas)


if __name__ == "__main__":

    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open('karaoke.smil'))
    print(sHandler.get_tags())
