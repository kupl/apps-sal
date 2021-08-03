def answer():
    if(n <= 60):
        all_ = set()
        for i in range(n):
            value = 0
            for j in range(i, n):
                value |= a[j]
                all_.add(value)
        if(len(all_) == n * (n + 1) // 2):
            return 'YES'
    return 'NO'


for T in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(answer())
