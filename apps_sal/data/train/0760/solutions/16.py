# pradeep singh NIT trichy
# pradeepsng30@yahoo.com

p = 1000000007
mod = p


def fact(n):
    f = 1
    i = 2
    while (i <= n):
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
#	print sorted(master_list) #If you need a sanity check, feel free to leave out
    return total_count
    # end perm_count


def permuter(my_list):  # returns a list of lists
    lists_list = []

    for i in range(len(my_list)):
        for j in range(len(my_list)):
            temp_list = my_list[:]
            if i != j:
                temp_list[i], temp_list[j] = temp_list[j], temp_list[i]
            if temp_list not in lists_list:
                lists_list.append(list(temp_list))

    return lists_list


def modInv(x):
    y = pow(x, p - 2, p)
    return y


def numP(wordArray):

    letterOccurances = list()
# List of letters that have been counted in wordArray
    countedLetters = list()

    wordLength = len(wordArray)

    numerator = fact(wordLength) % mod

# Loops through wordArray, counts how many times a letter occurs, skips over
# already counted letters using a list of such letters (list updated each time)
    for letter in wordArray:
        if letter in countedLetters:
            continue
        letterOccurances.append(wordArray.count(letter))
        countedLetters.append(letter)

    # Denominator of final formula
    denominator = 1
    ANS = 1
    ANS = numerator
#	modInv(900)
#	print "here"
    for i in letterOccurances:
        ANS = ANS * modInv(fact(i)) % mod
        #denominator = (denominator * math.factorial(i))

    return ANS


def ans(a):
    #	print "here"
    if(len(a) < 4):
        return 0
#	return 0
    mylist = list(a)
    n = numP(mylist)
#	n=24
    m = perm_count(mylist, 2) % mod
    return (n * (n - m)) % mod


t = int(input())
# print t

while (t > 0):
    a = input()
#	print a
    print(ans(a))
    # print "\n"
    t = t - 1
# print perm_count(D,2)
