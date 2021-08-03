def split_in_parts(s, part_length):
    cnt = 0
    answer = ""
    for i in s:
        if cnt < part_length:
            answer += i
            cnt += 1
        else:
            answer = answer + " " + i
            cnt = 1
    return answer
