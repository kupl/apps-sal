n, d = list(map(int, input().split()))

a = [0] + list(map(int, input().split())) + [0]  # aumento de timer según estación
X = []
Y = []

for i in range(n):
    x, y = list(map(int, input().split()))  # Coordenadas de la estación i.
    X.append(x)
    Y.append(y)

mon = [-1] * n  # array para el monto necesario para llegar.
mon[0] = 0
Z = 0  # valor que permitirá entrar al loop

while Z == 0:
    Z = 1

    for i in range(n):  # estamos en estación i

        for j in range(1, n):  # queremos ir a estación j

            if i != j and mon[i] != -1:  # si no queremos ir a la misma estación y donde estamos pudimos llegar.
                costo = mon[i] + (abs(X[i] - X[j]) + abs(Y[i] - Y[j])) * d - a[j]  # nuevo costo necesario para ir de i a j.

                if mon[j] == -1 or costo < mon[j]:  # si el nuevo costo es menor que uno anterior, se guarda este o si antes no había ningun costo guardado.
                    mon[j] = costo
                    Z = 0  # volvemos a entrar al loop, esto asegura que todos los mon[] van a dejar de ser '1 y tendran un costo.
print(mon[-1])  # costo de llegar a la última estación.
