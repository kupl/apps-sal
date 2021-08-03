def find_middle(string):
    try:
        lst = []
        for i in string:
            if i.isdigit():
                lst.append(i)
        x = str(eval('*'.join(lst)))
        return int(str(x)[len(x) // 2]) if len(x) % 2 == 1 else int(str(x)[len(x) // 2 - 1] + str(x)[len(x) // 2])
    except:
        return -1
