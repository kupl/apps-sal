t = int(input())
for _ in range(t):
    x = input()
    binary = bin(int(x) - 1)[2:]
    print(2 ** len(binary))
