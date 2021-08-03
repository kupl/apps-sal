def solve(n):
    while(n > 0):
        e = n % 10
        if(e % 2 == 0):
            return 1
        n = n // 10
    return 0


for _ in range(int(input())):
    n = int(input())
    print(solve(n))
