
t = int(input())

for i in range(t):
    a, b, c = map(int, input().split())
    li = [a, b, c]
    li.sort()
    print(li[1])
