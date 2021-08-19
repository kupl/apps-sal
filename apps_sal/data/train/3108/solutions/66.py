def multi_table(number):
    ans = ''
    i = 1
    for i in range(1, 11):
        ans += f'{i} * {number} = {i * number}\n'
        i += i
    return ans[:-1]
