import re

full_number_regex = re.compile(r"^\d{4} \d{4}$")
part_number_regex = re.compile(r"\d{4} \d{4}")
def is_valid_HK_phone_number(number):
    return full_number_regex.match(number) is not None

def has_valid_HK_phone_number(number):
    return part_number_regex.search(number) is not None

