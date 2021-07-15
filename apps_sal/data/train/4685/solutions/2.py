def self_descriptive(num):
    digits = [int(d) for d in str(num)]
    return all(digits.count(i) == digits[i] for i in range(len(digits)))
