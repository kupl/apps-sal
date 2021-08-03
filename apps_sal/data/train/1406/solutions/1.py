for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    even, odd = 0, 0
    for i in range(n):
        count_of_q = bin(a[i]).count('1')
        if count_of_q % 2 == 0:
            even += 1
        else:
            odd += 1
    for i in range(k):
        q = int(input())
        count_of_i = bin(q).count('1')
        if count_of_i % 2 == 0:
            print(even, odd)
        else:
            print(odd, even)
