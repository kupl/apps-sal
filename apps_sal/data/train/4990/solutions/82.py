def solution(string, ending):
    odw_string = string[::-1]
    odw_ending = ending[::-1]
    if odw_ending in odw_string[:len(odw_ending)]:
        return True
    else:
        return False
