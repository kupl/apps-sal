def solution(string, ending):
    start = -len(ending)
    return True if start == 0 else string[start::] == ending
