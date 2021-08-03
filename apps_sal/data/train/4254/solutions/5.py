def solve(eq):
    answer = ""
    temp = ""
    for i in eq[::-1]:
        if i.isalnum():
            temp += i
        else:
            answer += temp[::-1] + i
            temp = ""
    answer += temp[::-1]
    return answer
