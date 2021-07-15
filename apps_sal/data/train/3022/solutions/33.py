def two_highest(arg1):
    print(arg1)
    try:
        if len(arg1) == 1:
            return arg1
        else:
            value1 = max(arg1)
            arg2 = []
            for i in arg1:
                if i != value1:
                    arg2.append(i)
            value2 = max(arg2)
            return [value1, value2]
    except ValueError:
        return []
