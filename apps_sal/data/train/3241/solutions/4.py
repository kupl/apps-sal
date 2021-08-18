def buy_newspaper(s1, s2):
    count, temp = 0, ""
    for index, c in enumerate(s2):
        if c not in s1:
            return -1

        while index < len(temp) and temp[index] != c:
            temp = temp[:index] + temp[index + 1:]

        if not temp or index == len(temp):
            temp += s1[s1.find(c):]
            count += 1

    return count
