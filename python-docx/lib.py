# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 23:23:52 2020

@author: Jacobo
"""

from glob import glob
from docx import Document

def listar(path, filtro=""):
    spath=path + filtro
    return glob(spath)       
    
def leer_tabla_documento (fichero):
    print ("------- Leyendo documento "+fichero)
    wordDoc = Document(fichero)

    for table in wordDoc.tables:
        for row in table.rows:
            for cell in row.cells:
                print (cell.text)
    print ("------- Fin documento "+fichero)