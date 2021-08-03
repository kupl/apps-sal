def increment_string(string):
    print(string)
    if len(string) != 0:
        if string[-1].isdigit():
            if string.isdigit():
                result = str(int(string) + 1).zfill(len(string))
            else:
                c = 0
                re_str = string[::-1]
                for i in re_str:
                    if i.isdigit() == False:
                        num = string[-c:]
                        result = string[:len(string) - len(num)] + str(int(num) + 1).zfill(len(num))
                        break
                    c += 1
        else:
            result = string + '1'
    else:
        result = string + '1'
    return result
