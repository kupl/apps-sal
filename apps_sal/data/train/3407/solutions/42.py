def palindrome_chain_length(n):
    count = 0
    num = str(n)
    rev_num = str(n)[::-1]
    sum = 0
    while num != rev_num:
        num = str(int(num) + int(rev_num))
        rev_num = num[::-1]
        count += 1
    return count
