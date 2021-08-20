def find_longest(arr):
    weishu = [1]
    for number in arr:
        count = 0
        while number != 0:
            number = number // 10
            count = count + 1
        weishu.append(count)
    a = max(weishu)
    for number1 in arr:
        number = number1
        count = 0
        while number != 0:
            number = number // 10
            count = count + 1
        print(count)
        if count == a:
            return number1
