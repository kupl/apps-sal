for _ in range(int(input())):
    (n, k) = map(int, input().split())
    msg = input()
    small_cnt = cap_cnt = 0
    for char in msg:
        if char.isupper():
            cap_cnt += 1
        elif char.islower():
            small_cnt += 1
    if small_cnt <= k and cap_cnt <= k:
        print('both')
    elif small_cnt <= k and small_cnt < cap_cnt:
        print('brother')
    elif cap_cnt <= k and cap_cnt < small_cnt:
        print('chef')
    elif small_cnt > k and cap_cnt > k:
        print('none')
