def solution(digits):
    b = digits
    start_rez = 0
    end_rez = 5
    max = 0

    while end_rez <= len(b) + 1:
        rez = b[start_rez:end_rez]
        if max < int(rez):
            max = int(rez)
            if end_rez < len(b):
                start_rez += 1
                end_rez += 1
        else:
            start_rez += 1
            end_rez += 1
    return int(max)
