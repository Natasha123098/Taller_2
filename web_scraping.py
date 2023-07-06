import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:8000/'
#obtengo la pagina a analiza
html_doc = requests.get(url)
#print(html_doc.text)
#parsear la pagina web
soup = BeautifulSoup(html_doc.text, 'html.parser')

titulo_datos = soup.h1.string
print(titulo_datos)

tabla = soup.find('table')

#obtener las filas de la tabla
filas = tabla.find_all('tr')

nombres = []
apellidos = []
email = []

#iterar sobre las filas e imprimir los datos
#for fila in filas:
    #obtener las celdas de la tabla
    #celdas = fila.find_all('td')

    #extraer los datos de las celdas
    #datos = [celda.get_text(strip=True) for celda in celdas]

    #imprimir los datos
    #print(datos)

for fila in filas:
    celdas = fila.find_all('td')
    if len(celdas)>0:
        nombres.append(celdas[1].string)
        apellidos.append(celdas[2].string)
        email.append(celdas[4].string)

print(nombres)
print(apellidos)
print(email)

df = pd.DataFrame({'Nombres': nombres, 'Apellidos': apellidos, 'Email': email})
df.to_csv('doctores.csv', index=False, encoding='utf-8')

