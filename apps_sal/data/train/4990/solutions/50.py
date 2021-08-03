def solution(string, ending):
    if ending not in string:
        return False
    for a, b in zip(string[::-1], ending[::-1]):
        if a != b:
            return False
    return True
