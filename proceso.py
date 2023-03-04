# Programa entregar un número de 3 digitos inverso

print("-----------------------------------")
print("--------Reflejar numero------------")
print("-----------------------------------")

#input
a= int(input("Digite el valor de a: "))
b= int(input("Digite el valor de b: "))

if a==0:
  print(" es indeterminado")
else:
  x = -(b/a)

  print(" El punto de corte es:" + str(x))