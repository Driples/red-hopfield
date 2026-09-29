#Sergio Alfonso Casillas Santoyo - A01424863

import sys

M = 8
N = 5
n = M * N

patrones = ["cuadro", "cruz", "triangulo"]

if len(sys.argv) > 1:
    objetivo = sys.argv[1]
else:
    objetivo = "x"


def leer(nombre):
    archivo = open("dataset/" + nombre + ".txt", "r")
    vector = []
    for linea in archivo:
        for valor in linea.split():
            if valor == "1":
                vector.append(1)
            else:
                vector.append(-1)
    archivo.close()
    return vector


def imprimir(U):
    i = 0
    while i < M:
        fila = ""
        j = 0
        while j < N:
            if U[i * N + j] == 1:
                fila = fila + "# "
            else:
                fila = fila + ". "
            j += 1
        print(fila)
        i += 1
    print()


def F(x, actual):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return actual


X = []
for nombre in patrones:
    X.append(leer(nombre))

T = []
for i in range(n):
    fila = []
    for j in range(n):
        if i == j:
            fila.append(0)
        else:
            suma = 0
            for p in range(len(X)):
                suma = suma + X[p][i] * X[p][j]
            fila.append(suma)
    T.append(fila)

print("Patrones almacenados:")
for p in range(len(X)):
    print(patrones[p])
    imprimir(X[p])

U = leer(objetivo)
t = 0
print("U(" + str(t) + ") = " + objetivo)
imprimir(U)

anteriores = [U]
while True:
    nuevo = []
    for j in range(n):
        suma = 0
        for i in range(n):
            suma = suma + U[i] * T[i][j]
        nuevo.append(F(suma, U[j]))

    t += 1
    print("U(" + str(t) + ")")
    imprimir(nuevo)

    if nuevo == U:
        print("U(" + str(t) + ") = U(" + str(t - 1) + ")  =>  FIN")
        break
    elif nuevo in anteriores:
        print("La red entro en un ciclo  =>  FIN")
        break
    elif t >= 100:
        print("Se alcanzo el maximo de iteraciones  =>  FIN")
        break

    anteriores.append(nuevo)
    U = nuevo

reconocido = "ninguno"
for p in range(len(X)):
    if U == X[p]:
        reconocido = patrones[p]

print("Figura reconocida: " + reconocido)
