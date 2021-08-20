p = 1000000007
mod = p


def fact(n):
    f = 1
    i = 2
    while i <= n:
        f = f * i
        f = f % mod
        i = i + 1
    return f


def perm_count(orig_list, k):
    master_list = []
    master_list.append(list(orig_list))
    while k > 0:
        big_list = list(master_list)
        for each_list in big_list:
            for each_temp_list in permuter(each_list):
                if each_temp_list not in master_list:
                    master_list.append(each_temp_list)
        k -= 1
    total_count = len(master_list)
    return total_count


def permuter(my_list):
    lists_list = []
    for i in range(len(my_list)):
        for j in range(len(my_list)):
            temp_list = my_list[:]
            if i != j:
                (temp_list[i], temp_list[j]) = (temp_list[j], temp_list[i])
            if temp_list not in lists_list:
                lists_list.append(list(temp_list))
    return lists_list


def modInv(x):
    y = pow(x, p - 2, p)
    return y


def numP(wordArray):
    letterOccurances = list()
    countedLetters = list()
    wordLength = len(wordArray)
    numerator = fact(wordLength) % mod
    for letter in wordArray:
        if letter in countedLetters:
            continue
        letterOccurances.append(wordArray.count(letter))
        countedLetters.append(letter)
    denominator = 1
    ANS = 1
    ANS = numerator
    for i in letterOccurances:
        ANS = ANS * modInv(fact(i)) % mod
    return ANS


def ans(a):
    if len(a) < 4:
        return 0
    mylist = list(a)
    n = numP(mylist)
    m = perm_count(mylist, 2) % mod
    return n * (n - m) % mod


t = int(input())
while t > 0:
    a = input()
    print(ans(a))
    t = t - 1
