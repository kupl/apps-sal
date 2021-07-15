def reverse_str(str):
    return str[::-1]


def vert_mirror(strng):
    string_list = strng.split("\n")
    result = ""
    for i, element in enumerate(string_list):
        result = result + reverse_str(element)
        if i != len(string_list) - 1:
            result += "\n"
    return result

def hor_mirror(strng):
    string_list = strng.split("\n")
    result = ""
    for i, element in enumerate(string_list):
        result = element + result
        if i != len(string_list) - 1:
            result = "\n" + result 
    return result
    
def oper(fct, s):
    return fct(s)

