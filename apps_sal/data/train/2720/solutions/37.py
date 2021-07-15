def solution(digits):
    digit_ints = [int(x) for x in digits]
    max_digit = max(digit_ints)
    max_locs = [i for i in range(len(digits)) if digit_ints[i] == max_digit and i <= len(digits) - 5]
    while max_locs == []:
        max_digit -= 1
        max_locs = [i for i in range(len(digits)) if digit_ints[i] == max_digit and i <= len(digits) - 5]
    return max([int(digits[loc:loc + 5]) for loc in max_locs])
