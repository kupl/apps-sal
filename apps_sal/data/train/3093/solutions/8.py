def insert_dash(num):
    num = str(num)
    ans = ""
    for i in range(len(num) - 1):
        ans += num[i]
        if int(num[i]) % 2 == 1 and int(num[i + 1]) % 2 == 1:
            ans += '-'
    ans += num[-1]
    return ans

