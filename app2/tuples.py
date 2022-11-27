#las tuplas son inmutables, no se pueden cambiar
#las tuplas van entre parentecis

x = tuple((1,'r'))

y = tuple((1,2,3))

print(type(x))

print(y)

del x

x = [1,'r']

x[1] = 'm'

print(x[1])