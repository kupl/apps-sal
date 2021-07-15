n = int(input())
prizes = [1 for i in range(n)]
for j in range(int(n**(1/2))):
    if prizes[j] == 1:
        for i in range(2*j+2, n, j+2):
            prizes[i] = 2
if n > 2:
    print(2)
else:
    print(1)
for num in prizes:
    print(num, end=' ')
