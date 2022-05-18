import sqlite3
 
conn = sqlite3.connect('db.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS info(id INTEGER PRIMARY KEY ASC, carpeta INTEGER ,textIdioma TEXT, textOriginal TEXT, url TEXT)")
c.execute("CREATE TABLE IF NOT EXISTS carpetas(id INTEGER PRIMARY KEY ASC, padre INTEGER, nombre TEXT, idioma TEXT)")

def crearCarpetaRaiz(nombre, idioma):
    c.execute("INSERT INTO carpetas(padre, nombre, idioma) VALUES (0,"+ nombre +","+ idioma+")")

def crearSubCarpeta(padre, nombre, idioma):
    c.execute("INSERT INTO carpetas(padre, nombre, idioma) VALUES ("+ padre +","+ nombre +","+ idioma+"  )")

def guardar(carpeta, textIdioma, textOriginal):
    
