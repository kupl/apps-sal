def f(num):
    dic = {}
    while True:
        for i in range(2, int(num **0.5)+1):
            if num % i == 0:
                num /= i
                if i in dic:
                    dic[i] += 1
                else:
                    dic[i] = 1
                break
        else:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
            break
        continue
    ans = 1
    for item in dic:
        ans *= dic[item] * item ** (dic[item] - 1)
    return ans
