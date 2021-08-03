def palindrome_chain_length(n):
    cnt = 0
    while(str(n) != str(n)[::-1]):
        n = n + int(str(n)[::-1])
        cnt = cnt + 1
    return cnt
