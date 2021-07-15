def square_sum(numbers):
    li = []
    for x in numbers:
        x2 = x**2
        li.append(x2)
    add = sum(li[:])
    return add
