import re
number_pattern = re.compile("-?[0-9]+")

def string_to_int_list(s):
    return [int(c) for c in s.split(",") if re.match(number_pattern, c)]


