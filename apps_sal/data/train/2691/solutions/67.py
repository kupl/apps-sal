def solve(s):
    int_temp = []
    int_store = []
    for i in range(len(s)):
        try:
            int(s[i])
            int_temp.append(s[i])
            if i == len(s) - 1:
                int_store.append(''.join(int_temp))
        except:
            if int_temp == '':
                int_temp = []
            else:
                int_store.append(''.join(int_temp))
                int_temp = []
    int_clean = [int(x) for x in int_store if x not in '']
    return int(sorted(int_clean, reverse=True)[0])
