def pre_fizz(n):
    new_list = list()
    if n == 1:
        new_list1 = [n]
        return new_list1
    for numbers in range(1,n+ 1):
        new_list.append(numbers)
    return new_list
