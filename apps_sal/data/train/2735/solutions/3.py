def jumping_number(number):
    lst = list(map(int, str(number)))
    return "Jumping!!" if len(lst) == 1 or {1} == {abs(b - a) for a, b in zip(lst, lst[1:])} else "Not!!"
