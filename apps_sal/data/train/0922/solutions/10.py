def CountFrequency(my_list):
    freq = {}
    vec = []
    for item in my_list:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    for (key, value) in list(freq.items()):
        if value == 1:
            vec.append(key)
    vec.sort()
    return vec


t = int(input())
for i in range(0, t):
    (n, m) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = a + b
    ll = CountFrequency(c)
    print(*ll)
