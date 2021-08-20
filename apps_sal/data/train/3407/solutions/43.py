def palindrome_chain_length(n):
    sum = 0
    count = 0
    print('The number is ' + str(n))
    new_num = str(n)[::-1]
    if str(n) == str(n)[::-1]:
        return 0
    else:
        while str(n) != str(sum):
            sum = n + int(new_num)
            n = sum
            new_num = str(sum)[::-1]
            sum = int(new_num)
            count += 1
        return count
