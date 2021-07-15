def palindrome_chain_length(n):
    count = 0
    check = str(n)
    while check != check[::-1]:
        print(check)
        print(count)
        count += 1
        check = str(int(check) + int(check[::-1]))
    return count
