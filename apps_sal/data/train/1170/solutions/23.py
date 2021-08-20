for __ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    d = list(map(int, input().split()))
    st1 = ''
    for i in d:
        st1 += '1' if i % k == 0 else '0'
    print(st1)
