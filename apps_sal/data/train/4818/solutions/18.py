'''
'''


def solution(a, b):
    combined_string = ''
    if len(a) > len(b):
        combined_string = b + a + b
        return combined_string
    else:
        combined_string = a + b + a
        return combined_string
