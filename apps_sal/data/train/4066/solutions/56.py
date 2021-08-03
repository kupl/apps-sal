def string_to_array(s):
    words = ""
    answer = []
    for i in s:
        if i == " ":
            answer.append(words)
            words = ""
        else:
            words += i
    answer.append(words)
    return answer
