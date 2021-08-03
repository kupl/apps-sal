# Problem F - Zuma


n = int(input())
seg = n - 1
gemstones = [0] * 501
i = 0
for j in input().split(' '):
    gemstones[i] = int(j)
    i += 1
matriz = [[0] * 501 for i in range(501)]

for k in range(1, n + 1):
    ini = 0
    fim = k - 1
    while (fim < n):
        if (k == 1):
            matriz[ini][fim] = 1

        else:
            matriz[ini][fim] = matriz[ini + 1][fim] + 1

            if (gemstones[ini] == gemstones[ini + 1]):
                matriz[ini][fim] = min(matriz[ini][fim], matriz[ini + 2][fim] + 1)

            for l in range(ini + 2, fim + 1):
                if (gemstones[ini] == gemstones[l]):
                    matriz[ini][fim] = min(matriz[ini][fim], matriz[ini + 1][l - 1] + matriz[l + 1][fim])
        ini += 1
        fim += 1

print(matriz[0][seg])
