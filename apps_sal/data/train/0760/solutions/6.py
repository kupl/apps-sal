import math


def combi(a, b):
    if a < b:
        return 0
    if a == 1:
        return 1
    if b < a / 2:
        b = a - b
    temp = 1
    for i in range(b + 1, a + 1):
        temp *= i
    temp /= math.factorial(a - b)
    return temp


for _ in range(eval(input())):
    mod = 10 ** 9 + 7
    string1 = input()
    n = len(string1)
    dict1 = {}
    count = 0
    alpha = set()
    for ele in string1:
        if ele in dict1:
            dict1[ele] += 1
        else:
            dict1[ele] = 1
            alpha.add(ele)
            count += 1
    count_list = []
    total = 1
    rem = n
    for ele in alpha:
        total = total % mod * (combi(rem, dict1[ele]) % mod) % mod
        rem -= dict1[ele]
        count_list.append(dict1[ele])
    sum_list = [n - count_list[0]]
    for i in range(1, count):
        sum_list.append(sum_list[i - 1] - count_list[i])
    sub_2 = 0
    sub = 0
    for i in count_list:
        sub_2 += (n - i) * i
    sub_2 /= 2
    sub_3 = 0
    for i in range(count):
        for j in range(i + 1, count):
            sub_3 += count_list[i] * count_list[j] * sum_list[j]
    sub_3 = 2 * sub_3
    sub_4_4 = 0
    for i in range(count):
        for j in range(i + 1, count):
            for k in range(j + 1, count):
                sub_4_4 += count_list[i] * count_list[j] * count_list[k] * sum_list[k]
    sub_4_4 *= 3
    sub_4_2 = 0
    for i in range(count):
        for j in range(i + 1, count):
            sub_4_2 += count_list[i] * (count_list[i] - 1) * count_list[j] * (count_list[j] - 1) / 4
    sub_4_3 = 0
    for i in range(count):
        temp = 0
        for j in range(count):
            if j != i:
                temp += count_list[j] * (n - count_list[i] - count_list[j])
        temp /= 2
        sub_4_3 += count_list[i] * (count_list[i] - 1) * temp / 2
    sub_4_3 *= 2
    print(total * (total - 1 - (((sub_3 + sub_2) % mod + (sub_4_4 + sub_4_3) % mod) % mod + sub_4_2 % mod)) % mod)
