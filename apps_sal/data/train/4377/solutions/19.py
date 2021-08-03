def solve(a, b):
    count_a = 0
    count_b = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            count_a += 1
        elif a[i] < b[i]:
            count_b += 1
    return f'{count_a}, {count_b}: that looks like a "draw"! Rock on!' if count_a == count_b else f'{count_a}, {count_b}: Alice made "Kurt" proud!' if count_a > count_b else f'{count_a}, {count_b}: Bob made "Jeff" proud!'
