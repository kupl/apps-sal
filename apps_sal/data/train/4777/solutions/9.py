def mystery_range(string, length_of_range, numbers_already_found=[]):
    if string == '':
        return [min(numbers_already_found), max(numbers_already_found)]
    for next_number_length in [1, 2, 3]:
        if len(string) < next_number_length or string.startswith('0'):
            return False
        next_number_candidate = int(string[:next_number_length])
        if next_number_candidate not in numbers_already_found and (numbers_already_found == [] or (next_number_candidate - min(numbers_already_found) < length_of_range and max(numbers_already_found) - next_number_candidate < length_of_range)):
            result = mystery_range(string[next_number_length:], length_of_range, numbers_already_found + [next_number_candidate])
            if result != False:
                return result
    return False
