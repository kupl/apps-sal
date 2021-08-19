# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())

    total = round((n * (n - 1)) / 2)
    if total % n == 0:
        print("YES")
        win = round(total / n)
        matches = [['0'] * n for _ in range(n)]

        s_pos = 1
        for r in range(n):
            c_pos = s_pos
            for c in range(win):
                #print(f'Row : {r}, Col : {c_pos}')
                matches[r][c_pos] = '1'
                # print(matches[r][c_pos])
                # print(matches)
                c_pos = (c_pos + 1) % n

            s_pos = (s_pos + 1) % n

        for itr in matches:
            print(''.join(itr))
    else:
        print("NO")
