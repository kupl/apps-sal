def seven_ate9(string):
    index = 0
    result = ''
    while index < len(string):
        if string[index] == '9':
            if index + 1 != len(string):
                if string[index - 1] == '7' and string[index + 1] == '7':
                    result += ''
                else:
                    result += string[index]
            else:
                result += string[index]
        else:
            result += string[index]
        index += 1
    return result
