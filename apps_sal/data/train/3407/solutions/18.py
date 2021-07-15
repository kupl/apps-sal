def palindrome_chain_length(n):
    counter, last_num = 0, n

    def reverse_num(a_num):
        return str(a_num)[::-1]

    def is_palindrome(sum_num):
        return reverse_num(sum_num) == str(sum_num)

    while not is_palindrome(last_num):
        last_num = last_num + int(reverse_num(last_num))
        counter += 1
        
    return counter
