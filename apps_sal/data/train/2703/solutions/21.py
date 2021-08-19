def square_sum(numbers):
    new_lst = []
    for i in numbers:
        i = i * i
        new_lst.append(i)
    return sum(new_lst)
