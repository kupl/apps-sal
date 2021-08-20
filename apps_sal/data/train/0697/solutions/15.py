t = int(input())
for _ in range(t):
    (n, k) = map(int, input().split())
    array = list(map(int, input().split()))
    massimo = sum(array[:k])
    appo = massimo
    for i in range(n - k):
        appo += array[k + i] - array[i]
        massimo = max(massimo, appo)
    print(massimo)
