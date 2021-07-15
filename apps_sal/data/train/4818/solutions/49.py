def solution(a, b):
    '''determine which string, (a or b) is longer and printing the, short, long, short'''
    if len(a) > len(b):
        return b + a + b
    else:
        return a + b + a
