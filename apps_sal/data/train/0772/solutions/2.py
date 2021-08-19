import itertools


def checkPalindrome(string):
    if string == string[::-1]:
        return 1
    else:
        return 0


t = int(eval(input()))
while t:
    ip_string = input()
    length_of_str = len(ip_string)
    p = 2
    count = length_of_str
    while p <= length_of_str:
        for i in range(1, length_of_str + 1):
            temp_str = ip_string[i - 1]
            indx_chk = str(i)
            j = i * p
            while j <= length_of_str:
                temp_str += ip_string[j - 1]
                indx_chk += str(j)
                if checkPalindrome(temp_str) == 1:
                    count += 1
                j = j * p
        p += 1
    print(count)
    t -= 1
