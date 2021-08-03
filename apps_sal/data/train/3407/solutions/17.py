def palindrome_chain_length(n):
    def calculate_palindrome(steps, n):
        if str(n)[::-1] == str(n):
            return steps
        else:
            return calculate_palindrome(steps + 1, n + int(str(n)[::-1]))
    return calculate_palindrome(0, n)
