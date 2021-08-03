def no_space(x):
    # your code here
    answer = ""
    for i in x:
        if i == " ":
            continue
        else:
            answer += i
    return answer
