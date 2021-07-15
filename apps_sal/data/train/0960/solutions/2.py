def solve(n):
    k=1
    for i in range(n):
        for j in range(n):
            print(bin(k).replace('0b',''),end=' ')
            k+=1
        print()
for _ in range(int(input())):
    n=int(input())
    solve(n)

