test = int(input())
while test != 0:
    test = test - 1
    (n, k) = list(map(int, input().split()))
    s = input()
    i = 0
    j = 0
    mag = 0
    sheet = 0
    while i < n and j < n:
        if s[i] == 'I':
            if s[j] == 'M':
                if i < j:
                    for a in range(i, j + 1):
                        if s[a] == ':':
                            sheet = sheet + 1
                if j < i:
                    for a in range(j, i + 1):
                        if s[a] == ':':
                            sheet = sheet + 1
                power = k + 1 - abs(j - i) + sheet
                sheet = 0
                if power > 0:
                    mag += 1
                    i += 1
                    j += 1
                elif i > j:
                    j += 1
                else:
                    i += 1
            elif s[j] == 'X':
                i = j
                i += 1
                j += 1
            else:
                j += 1
        elif s[i] == 'X':
            j = i
            j += 1
            i += 1
        else:
            i += 1
    print(mag)
