def value(a, b, c):
    if(c == '&'):
        return a&b
    elif(c == '^'):
        return a^b
    elif(c == '|'):
        return a|b

def break_rules(n, operator):
    if(len(n) == 1):
        return n
    elif(len(n) == 2):
        return [value(n[0], n[1], operator[0])]
    else:
        cont_ans = []
        for i in range(1,len(n)):
            l1 = n[:i]
            l2 = n[i:]
            o1 = operator[:i]
            o2 = operator[i:]
            l1_ans = break_rules(l1, o1)
            l2_ans = break_rules(l2, o2)
            for k in l1_ans:
                for j in l2_ans:
                    cont_ans.append(value(k, j, operator[i - 1]))
    return cont_ans

t = int(input())
while t > 0 :
    operator = []
    num = []
    exp = input()
    temp = ''
    for i in range(len(exp)):
        if(ord(exp[i]) > 47 and ord(exp[i]) < 58):
            temp = temp + exp[i]
        else:
            num.append(int(temp))
            temp = ''
            operator.append(exp[i])
        if(i == len(exp) - 1):
            num.append(int(temp))
    t -= 1
    # print(num,operator)
    print(max(break_rules(num, operator)))
