#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):

        self.diccionario_atributos = [["etiqueta", "width",
                                       "height", "background-color"],
                                      ["etiqueta", "id", "top", "bottom",
                                       "left", "right"],
                                      ["etiqueta", "src", "region", "begin",
                                       "dur"],
                                      ["etiqueta", "src", "begin", "dur"],
                                      ["etiqueta", "src", "region"]]

        self.lista_etiquetas = []

    def startElement(self, etiqueta, attrs):

        self.diccionario_atributos = {}
        self.diccionario_atributos["etiqueta"] = etiqueta

        if etiqueta == 'root-layout':
            self.root_layout_width = attrs.get('width', "")
            self.root_layout_height = attrs.get('height', "")
            self.root_layout_background_color = attrs.get('background-color'
                                                          ,"")
            self.diccionario_atributos["width"] = self.root_layout_width
            self.diccionario_atributos["height"] = self.root_layout_height
            self.diccionario_atributos["background-color"] = \
            self.root_layout_background_color
            self.diccionario_atributos["etiqueta"] = etiqueta
            self.lista_etiquetas.append(self.diccionario_atributos)

        elif etiqueta == 'region':
            self.region_id = attrs.get('id', "")
            self.region_top = attrs.get('top', "")
            self.region_bottom = attrs.get('bottom', "")
            self.region_left = attrs.get('left', "")
            self.region_right = attrs.get('right', "")
            self.diccionario_atributos["id"] = self.region_id
            self.diccionario_atributos["top"] = self.region_top
            self.diccionario_atributos["bottom"] = self.region_bottom
            self.diccionario_atributos["left"] = self.region_left
            self.diccionario_atributos["right"] = self.region_right
            self.diccionario_atributos["etiqueta"] = etiqueta
            self.lista_etiquetas.append(self.diccionario_atributos)

        elif etiqueta == 'img':
            self.img_src = attrs.get('src', "")
            self.img_region = attrs.get('region', "")
            self.img_begin = attrs.get('begin', "")
            self.img_dur = attrs.get('dur', "")
            self.diccionario_atributos["src"] = self.img_src
            self.diccionario_atributos["region"] = self.img_region
            self.diccionario_atributos["begin"] = self.img_begin
            self.diccionario_atributos["dur"] = self.img_dur
            self.diccionario_atributos["etiqueta"] = etiqueta
            self.lista_etiquetas.append(self.diccionario_atributos)

        elif etiqueta == 'audio':

            self.audio_src = attrs.get('src', "")
            self.audio_begin = attrs.get('begin', "")
            self.audio_dur = attrs.get('dur', "")
            self.diccionario_atributos["src"] = self.audio_src
            self.diccionario_atributos["begin"] = self.audio_begin
            self.diccionario_atributos["dur"] = self.audio_dur
            self.diccionario_atributos["etiqueta"] = etiqueta
            self.lista_etiquetas.append(self.diccionario_atributos)

        elif etiqueta == 'textstream':

            self.textstream_src = attrs.get('src', "")
            self.textstream_region = attrs.get('region', "")
            self.diccionario_atributos["src"] = self.textstream_src
            self.diccionario_atributos["region"] = self.textstream_region
            self.diccionario_atributos["etiqueta"] = etiqueta
            self.lista_etiquetas.append(self.diccionario_atributos)

    def get_tags(self):

        return (self.lista_etiquetas)


if __name__ == "__main__":

    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open('karaoke.smil'))
    print(sHandler.get_tags())
