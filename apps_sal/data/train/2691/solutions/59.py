def solve(s):
    number = 0
    lst = []
    last = 0
    for i in range(len(s)):
        if s[i].isnumeric():
            if last == i - 1:
                number = number * 10 + int(s[i])
                last = i
            else:
                lst.append(number)
                number = int(s[i])
                last = i
    lst.append(number)
    return max(lst)
