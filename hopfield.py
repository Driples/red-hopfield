#Sergio Alfonso Casillas Santoyo - A01424863

M = 8
N = 5
n = M * N


def leer(nombre):
    vector = []
    for valor in open("dataset/" + nombre + ".txt").read().split():
        if valor == "1":
            vector.append(1)
        else:
            vector.append(-1)
    return vector


def imprimir(U):
    for i in range(M):
        fila = ""
        for j in range(N):
            if U[i * N + j] == 1:
                fila = fila + "# "
            else:
                fila = fila + ". "
        print(fila)
    print()


patrones = ["cuadro", "cruz", "triangulo"]
X = []
for nombre in patrones:
    X.append(leer(nombre))

T = []
for i in range(n):
    fila = []
    for j in range(n):
        suma = 0
        if i != j:
            for p in X:
                suma = suma + p[i] * p[j]
        fila.append(suma)
    T.append(fila)

U = leer("x")
print("Entrada:")
imprimir(U)

cambio = True
while cambio:
    nuevo = []
    for j in range(n):
        suma = 0
        for i in range(n):
            suma = suma + U[i] * T[i][j]
        if suma > 0:
            nuevo.append(1)
        elif suma < 0:
            nuevo.append(-1)
        else:
            nuevo.append(U[j])
    cambio = nuevo != U
    U = nuevo

print("Salida:")
imprimir(U)

for p in range(len(X)):
    if U == X[p]:
        print("Figura reconocida: " + patrones[p])
