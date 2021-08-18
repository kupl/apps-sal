t = 0
try:
    t = int(input())
except:
    pass

for _ in range(t):
    a = input()

    print(len(set(a)))
