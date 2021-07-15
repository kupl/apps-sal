import re

# def replacenth(strings, elem, values, i):
#     find = strings.find(elem)
#     # If find is not -1 we have found at least one match for the substring
#     j = find != -1
#     # loop util we find the nth or we find no match
#     while find != -1 and j != i:
#         # find + 1 means we start searching from after the last match
#         find = strings.find(elem, find + 1)
#         j += 1
#     # If i is equal to n we found nth match so replace
#     if j == i:
#         return strings[:find] + values + strings[find+len(elem):]
#     return strings

def replacenth(string, elem, values, i):
    where = [m.start() for m in re.finditer(elem, string)][i-1]
    before = string[:where]
    after = string[where:]
    after = after.replace(elem, values, 1)
    newString = before + after
    return newString

def string_convertor(strings_options, tuples_options):
    new_list = []
    new_list.clear()
    
    for strings in strings_options:
        # Try to find the second string in tuple and replace in strings_options
        for elem, values in tuples_options:
            if elem in strings:
                count_strings = strings.count(elem)
                if count_strings == 1:
                    strings_options = strings.replace(elem, values, 1)
                    new_list.append(strings_options)
                else:
                    i = 0
                    while i != count_strings:
                        strings_options = replacenth(strings, elem, values, i)
                        new_list.append(strings_options)
                        i += 1
                    
        
    list_string_converted = new_list
    return list_string_converted


def word_problem(rules: List[Tuple[str, str]], from_str: str, to_str: str, applications: int) -> bool:

    print(("From", from_str, "to", to_str, "with", applications, "applications"))
    print(("Rules :", rules))

    if applications == 0:
        if from_str == to_str:
            return True
        else:
            return False

    elif applications >= 1:
        # Call string_convertor function the same number of times we've applications
        # except if before reaching this number we run out of options
        
        list_string_converted = from_str.split()
        print((list_string_converted, " -----------"))
        nb_try = 0

        while nb_try <= applications:
            try:
                print(("-while nb :", nb_try, "list cvd :", list_string_converted))
                # call the function and use list(set()) to remove doubles in list:
                list_string_converted = list(set(string_convertor(list_string_converted, rules)))
                nb_try += 1
                
                if not list_string_converted:
                    return False
                
                for elem in list_string_converted:    
                    if elem == to_str :
                        print(("Find it!", elem))
                        return True
                    
                    elif elem != to_str and nb_try == applications+1:
                        return False
                    else:
                        pass
            except:
                print("error")


