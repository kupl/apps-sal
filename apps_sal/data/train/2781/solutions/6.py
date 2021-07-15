def collatz_len(n):
    result = 1
    while n != 1:
        if n % 2:
            n = 3 * n + 1
        else:
            n //= 2
        result += 1
    return result

def longest_collatz(input_array):
    return max(input_array, key=collatz_len)
