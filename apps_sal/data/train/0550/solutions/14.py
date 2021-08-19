# cook your dish here
for i in range(int(input())):
    A, B = map(int, input().split())
    B = bin(B)[2:]
    B = list(map(str, B))
    for j in range(len(str(bin(A)[2:])) - len(B)):
        B.insert(0, "0")
    xor = A ^ int(("".join(B)), 2)
    max = xor
    c = 0
    for j in range(len(B) - 1):
        B = (B[-1:] + B[:-1])
        xor = A ^ int(("".join(B)), 2)
        if xor > max:
            max = xor
            c = j + 1
    print(c, max)
