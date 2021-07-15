
def solution(string, ending):
    tracker = 0
    for x in range(0, len(ending)):
        if len(string) >= len(ending):
            if string[-1-x] == ending[-1-x]:
                tracker += 1
    return tracker == len(ending)
