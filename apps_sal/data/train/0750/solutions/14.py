n = int(input())
while n:
    l = list(map(int, input().split()))
    invl = [None] * n
    for j in range(n):
        i = j + 1
        invl[l[j] - 1] = i
    for i in range(n):
        if l[i] != invl[i]:
            print("not ambiguous")
            break
    else:
        print("ambiguous")
    n = int(input())
