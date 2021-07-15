def seven_ate9(str_):
    ans = str_[0]
    for i in range(1, len(str_)-1):
        if str_[i] == '9' and str_[i-1] == '7' and str_[i+1] == '7':
            continue
        ans += str_[i]
    return ans + str_[-1]
