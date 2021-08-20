def do_math(s):
    alfavit = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def izvlech(s):
        s += ' '
        list = []
        string = ''
        for x in s:
            if x != ' ':
                string += x
            else:
                list.append(string)
                string = ''
        return list

    def izvlech1(list1, alfavit):
        list2 = []
        for z in alfavit:
            for x in list1:
                for y in x:
                    if z == y:
                        list2.append(x)
        return list2
    list1 = izvlech(s)
    list2 = izvlech1(list1, alfavit)
    result = ''
    final_result = 0
    index = 0
    for x in list2:
        for y in x:
            try:
                y = int(y)
                result += str(y)
            except ValueError:
                continue
        if index == 0:
            index += 1
            final_result = int(result)
            result = ''
            continue
        elif index == 1:
            final_result += int(result)
            result = ''
            index += 1
            continue
        elif index == 2:
            final_result -= int(result)
            result = ''
            index += 1
            continue
        elif index == 3:
            final_result *= int(result)
            result = ''
            index += 1
            continue
        elif index == 4:
            final_result /= int(result)
            result = ''
            index = 1
            continue
    return round(final_result)
