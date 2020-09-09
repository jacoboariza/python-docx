# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 21:29:07 2020

@author: Jacobo
"""

from lib import listar
from lib import leer_tabla_documento
from lib import getText

directorio="../"
filtro="*.docx"

files=listar(directorio, filtro)
for file in files:
    leer_tabla_documento(file)

print(getText("../prueba.docx"))
#archivo-salida.py

f = open ('salida.txt','w')
f.write(getText("../prueba.docx"))
f.close()