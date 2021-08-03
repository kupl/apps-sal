pow2 = []
for i in range(61):
    pow2.append(1 << i)
for _ in range(int(input())):
    x = int(input())
    for i in range(61):
        if x <= pow2[i]:
            print(pow2[i])
            break
