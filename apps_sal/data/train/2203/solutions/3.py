v = [max(map(int, input().split())) for i in range(int(input()))]
v[v.index(max(v))] += 1
print(' '.join(map(str, v)))
