n = int(input())
p = list(zip(map(int,input().split()),map(int,input().split()),map(int,input().split())))
p.sort()
pointer = [-1,0,0,0]
input()
for cj in map(int,input().split()):
    while pointer[cj] < n and (p[pointer[cj]] == None or cj not in p[pointer[cj]][1:]):
        pointer[cj]+= 1
    if pointer[cj] == n:
        print(-1, end=' ')
    else:
        print(p[pointer[cj]][0], end=' ')
        p[pointer[cj]] = None
