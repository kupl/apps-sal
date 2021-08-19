cases = int(input())
for case in range(cases):
    n = int(input())
    freq = [0] * 10001
    a = list(map(int, input().split()))
    largest = 1
    for i in range(n):
        freq[a[i]] += 1
        largest = max(largest, a[i])
    most = 0
    for num in range(largest + 1):
        if freq[num] > freq[most]:
            most = num
    print(most, freq[most])
