#print('info')
#dir(x) 
#type(11) number

def hola(x='x',y=''):
    nac = int(2022) - int(y)
    if x != '':
        print('hola {0}'.format(x))
    print('tu edad es {0}'.format(y))
    print('tu anio de nacimiento es {0}'.format(nac))





edad = input("Edad ? : ")
nombre = input("Nombre ? : ")
edad = int(edad)

hola(nombre,edad)















