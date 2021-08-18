for _ in range(int(input())):
    s = input()
    count = 0
    i = 0
    while i < len(s) - 1:
        ch = s[i]
        j = i + 1
        while j < len(s) and s[j] == ch:
            j += 1
        l = j - i
        if i != 0 and j != len(s) and s[i - 1] == s[j]:
            count += 1
        count += l * (l - 1) // 2
        i = j
    print(count)
