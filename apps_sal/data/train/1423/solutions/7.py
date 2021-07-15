t = int(input())
for test in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())
    k -= 1
    element = a[k]
    a.sort()
    element_index = a.index(element)
    element_index += 1
    print(element_index)
