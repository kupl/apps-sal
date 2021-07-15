n = int(input())
le = 2*n-1
for i in range(le):
    for j in range(le):
        print(n- min(i,j,le-1-i,le-1-j),end=' ')
    print()

