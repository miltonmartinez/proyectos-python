import requests  #Importamos la librería requests

print("SOLICITANDO INFORMACION DE INTERNET")
print("espere....") 
URL = 'https://restcountries.com/v2/all' #configuramos la url
#solicitamos la información y guardamos la respuesta en data.
data = requests.get(URL) 

data = data.json() #convertimos la respuesta en dict

print(data)

for element in data: #iteramos sobre data
    print(element['name']) #Accedemos a sus valores