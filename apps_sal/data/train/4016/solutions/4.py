def game(a, b):
    if a == 0 or b == 0:
        return "Non-drinkers can't play"
    sum_a = 0
    sum_b = 0
    i = 1
    while sum_a <= a and sum_b <= b:
        if i % 2 != 0:
            sum_a += i
        else:
            sum_b += i
        i += 1
    if sum_a > a:
        return 'Joe'
    if sum_b > b:
        return 'Mike'
