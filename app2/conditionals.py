
x = input("Edad ? : ")

x = int(x)

if x < 30:
    print("{0} es menor que 30".format(x))
elif x == 50 and x > 30:
    print("{0} es igual que 50".format(x))
else:
    print("{0} es mayor que 30".format(x))

