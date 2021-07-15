def seven(m):
    if m == 0:
        return (0,0)
    else:
        try:
            count = 0
            while len(str(m)) != 2:
                if len(str(m)) == 1 and m % 7 != 0:
                    return (res,count)
                else:
                    where_to_stop = len(str(m))-1
                    first_part = str(m)
                    first_part = first_part[:where_to_stop]
                    second_part = str(m)[where_to_stop]
                    res = int(first_part) - 2*int(second_part)
                    m = res
                    count += 1
                    if m % 7 == 0 and len(str(m)) <= 2:
                        return (res,count)
            return (res,count)
        except:
            print(m)
