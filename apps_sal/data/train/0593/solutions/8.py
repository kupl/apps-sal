for _ in range(int(input())):
    A = list(map(int, input().split()))
    s, x = list(set(list(input()))), 0
    for c in s:
        x += A[ord(c) - 97]
    print(sum(A) - x)
