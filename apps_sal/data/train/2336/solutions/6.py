n = int(input())
a = list(map(int, input().split()))
if sum(a[i] == i + 1 for i in range(n)) >= n // 1000:
    print("Petr")
else:
    print("Um_nik")
