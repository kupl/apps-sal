import re


def replacenth(string, elem, values, i):
    where = [m.start() for m in re.finditer(elem, string)][i - 1]
    before = string[:where]
    after = string[where:]
    after = after.replace(elem, values, 1)
    newString = before + after
    return newString


def string_convertor(strings_options, tuples_options):
    new_list = []
    new_list.clear()
    for strings in strings_options:
        for (elem, values) in tuples_options:
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
    if applications == 0:
        if from_str == to_str:
            return True
        else:
            return False
    elif applications >= 1:
        list_string_converted = from_str.split()
        nb_try = 0
        while nb_try <= applications:
            try:
                list_string_converted = list(set(string_convertor(list_string_converted, rules)))
                nb_try += 1
                if not list_string_converted:
                    return False
                for elem in list_string_converted:
                    if elem == to_str:
                        return True
                    elif elem != to_str and nb_try == applications + 1:
                        return False
                    else:
                        pass
            except:
                pass
