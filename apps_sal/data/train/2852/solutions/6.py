
def find_longest(string):
    n = len(string)

    stk = []
    stk.append(-1)

    result = 0

    for i in range(n):

        if string[i] == '(':
            stk.append(i)

        else:

            stk.pop()

            if len(stk) != 0:
                result = max(result, i - stk[len(stk) - 1])

            else:
                stk.append(i)

    return result
