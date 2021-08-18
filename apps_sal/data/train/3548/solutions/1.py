import re


def poly(lst):
    ans = [1, -lst.pop()]
    while lst:
        ans.append(0)
        r = lst.pop()
        for i in range(len(ans) - 1, 0, -1):
            ans[i] -= r * ans[i - 1]
    return ans


def polynomialize(roots):
    if len(roots) == 1:
        if roots[0] == 0:
            return 'x = 0'
        elif roots[0] < 0:
            return 'x + ' + str(abs(roots[0])) + ' = 0'
        else:
            return 'x - ' + str(roots[0]) + ' = 0'
    if len([i for i in roots if i != 0]) == 0:
        return 'x^' + str(len(roots)) + ' = 0'

    ans = poly(roots)
    ans1 = ans[:]

    final = []
    for i in range(len(ans[:-1])):
        try:
            if int(ans[i]) == 0:
                continue
        except:
            continue
        if int(ans[i]) == 1:
            num = len(ans1[:-1]) - i
            if num == 1:
                final.append('x')
            else:
                final.append('x^{}'.format(str(num)))
        else:
            num = len(ans1[:-1]) - i
            if num == 1:
                final.append(str(int(ans[i])) + 'x')
            else:
                final.append(str(int(ans[i])) + 'x^{}'.format(str(num)))
    if int(ans[-1]) != 0:
        final.append(str(int(ans[-1])))
    if isinstance(final[0], list):
        final = final[-1]
    answer = '+'.join(final)

    answer = answer.replace('+-', ' - ')
    answer = answer.replace('+', ' + ')
    answer = re.sub(" 1x", ' x', answer)
    return answer + ' = 0'
