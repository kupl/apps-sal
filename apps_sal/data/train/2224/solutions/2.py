n = int(input())
a = input()
b = input()
zo = {(0, 0): 0, (0, 1): 0, (1, 0): 0, (1, 1): 0}
for c, d in zip(a, b):
    zo[int(c), int(d)] += 1

print(zo[0, 0] * (zo[1, 0] + zo[1, 1]) + zo[1, 0] * zo[0, 1])

