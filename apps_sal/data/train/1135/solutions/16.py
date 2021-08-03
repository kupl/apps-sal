''' author: Priyank Koul, PES University, Bengaluru'''
for _ in range(int(input())):
    n, k = list(map(int, input().strip().split()))
    a = n - k
    for i in range(a, n + 1):
        print(i, end=" ")
    for i in range(1, a):
        print(i, end=" ")
    print("")
