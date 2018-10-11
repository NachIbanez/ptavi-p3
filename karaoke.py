#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from smallsmilhandler import SmallSMILHandler
import sys
import json
import urllib.request


class KaraokeLocal(SmallSMILHandler):

    def __init__(self, file):
        parser = make_parser()
        sHandler = SmallSMILHandler()
        parser.setContentHandler(sHandler)
        parser.parse(open(file))
        self.lista = sHandler.get_tags()

    def __str__(self):
        num_elemento = 1
        self.cadena = ""
        for diccionario in self.lista:
            self.cadena += ("-Elemento" + str(num_elemento) + 
                       ":" + diccionario["etiqueta"])
            atributos = list(diccionario)
            for atributo in atributos:
                if atributo != "etiqueta" and diccionario[atributo] != "":    
                    self.cadena += ("\t" + atributo + "=" + diccionario[atributo])
            self.cadena += ("\n")
            num_elemento += 1
        return self.cadena

    def to_json(self):
        json_file = json.dumps(Karaoke.lista)
        karaoke_json = open("karaoke.json", "w")
        karaoke_json.write(json_file)
        
    def do_local(self):
        for diccionario in self.lista:
            atributos = list(diccionario)
            for atributo in atributos:
                if atributo == "src" and diccionario[atributo][:7] == "http://":
                    url = diccionario[atributo]
                    url_reves = diccionario[atributo][::-1]
                    index = url_reves.index("/")
                    file_name = url_reves[:index][::-1]
                    urllib.request.urlretrieve(url, file_name)
                    diccionario[atributo] = file_name 
        return self.lista
     
if __name__ == "__main__":
 
    try:
         fichero = (sys.argv[1])   
    except IndexError:
            sys.exit("Usage: python3 karaoke.py file.smil")

    Karaoke = KaraokeLocal(fichero)
    print(Karaoke)
    Karaoke.to_json()
    print("---------------------------------------------------------------\n")
    Karaoke.do_local()
    print(Karaoke)
