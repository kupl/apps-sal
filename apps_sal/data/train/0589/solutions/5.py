T = int(input())
for t in range(T):
    s = input()
    L = len(s)
    days = 0
    i = 0
    jump_len_known = 1
    while i < L:
        while i < L and s[i] == '#':
            i += 1
        if i < L:
            j = i + 1
            while j < L and s[j] == '.':
                j += 1
            jump_len = j - i + 1
            if jump_len_known < jump_len:
                days += 1
                jump_len_known = jump_len
            i = j
    print(days)
