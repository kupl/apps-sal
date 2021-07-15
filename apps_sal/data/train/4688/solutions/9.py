def expanded_form(num):
    num = str(num)
    index = num.index('.')
    leng = len(num) - index - 1
    num = num[:index] + num[index + 1:]
    ans1 = ' + '.join(num[i] + (index-i-1) * '0' for i in range(index) if num[i] != '0')
    ans2 = ' + '.join(num[i+index] + '/1' + (i+1) * '0' for i in range(leng) if num[i+index]!='0')
    return ans2 if not ans1 else ans1 + ' + ' + ans2
