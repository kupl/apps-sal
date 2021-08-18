def string_to_number(s):
    ans = 0
    counter = 1
    for i in s[::-1]:
        if i == '-':
            ans *= -1
        else:
            ans += int(i) * counter
            counter *= 10
    return ans
