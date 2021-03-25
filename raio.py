PI = 3.141592
raio = float(input(""))
circuferencia = 2  * PI * raio
a_circulo = PI * (raio * raio)
a_esfera = 4 * PI * raio ** 2
vol_esfera = 4/3 * PI * raio ** 3

print("%.6f" % circuferencia)
print("%.6f" % a_circulo)
print("%.6f" % a_esfera)
print("%.6f" % vol_esfera)
