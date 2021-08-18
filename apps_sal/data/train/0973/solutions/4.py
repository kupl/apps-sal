a = int(input())
z = []
for i in range(a):
    b = input().split()
    c = list(map(int, input().split()))
    z.append(max(c) - min(c) + 2 * int(b[1]))
for i in z:
    print(i)
