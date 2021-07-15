for _ in range(int(input())):
    n = int(input())
    s = input()
    st = 0
    fans = 0
    for x in s:
        if x == ')':
            st -= 1
        else:
            st += 1
        if st < 0:
            fans += 1
            st = 0
    print(fans)
