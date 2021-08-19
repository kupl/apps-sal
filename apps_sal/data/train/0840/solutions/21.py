# cook your dish here
t = int(input())
for _ in range(t):
    k = int(input())
    i = 0
    l = k - 1
    for j in range(k):
        print((" " * min(i, l)) + "*")
        i += 1
        l -= 1
