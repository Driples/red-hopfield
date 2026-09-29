#Sergio Alfonso Casillas Santoyo - A01424863

T = [
    [0, 2, 2, -2],
    [2, 0, 2, -2],
    [2, 2, 0, -2],
    [-2, -2, -2, 0]
]

n = 4
U = [-1, -1, -1, -1]


def F(x, actual):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return actual


t = 0
print("U(" + str(t) + ") =", U)

while True:
    neto = []
    j = 0
    while j < n:
        suma = 0
        i = 0
        while i < n:
            suma = suma + U[i] * T[i][j]
            i += 1
        neto.append(suma)
        j += 1

    print("U(" + str(t) + ").T =", neto)

    nuevo = []
    k = 0
    while k < n:
        nuevo.append(F(neto[k], U[k]))
        k += 1

    t += 1
    print("U(" + str(t) + ") =", nuevo)

    igual = True
    k = 0
    while k < n:
        if nuevo[k] != U[k]:
            igual = False
        k += 1

    U = nuevo

    if igual:
        print("U(" + str(t) + ") = U(" + str(t - 1) + ")  =>  FIN")
        break