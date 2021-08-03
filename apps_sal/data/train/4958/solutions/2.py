def solution(value):
    num = 5 - len(str(value))
    zeros = ""
    for i in range(num):
        zeros += "0"
    return("Value is {}".format(zeros + str(value)))
