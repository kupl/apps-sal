T = int(input())

for i in range(T):
    N = int(input())
    Number = ""
    for l in range(1, N + 1):
        Number += str(l)
    Multiply = 1
    for j in range(len(Number)):
        Multiply = Multiply * int(Number[j])
    print(Multiply)
