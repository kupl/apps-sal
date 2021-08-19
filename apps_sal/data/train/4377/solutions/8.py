def solve(a, b):
    count_A = 0
    count_B = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            count_A += 1
        elif a[i] < b[i]:
            count_B += 1
    return f'{count_A}, {count_B}: that looks like a "draw"! Rock on!' if count_A == count_B else f'{count_A}, {count_B}: Alice made "Kurt" proud!' if count_A > count_B else f'{count_A}, {count_B}: Bob made "Jeff" proud!'
