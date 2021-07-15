def solution(digits):
    number = str(digits)
    max_seq = ''
    for i in range(len(number) - 3):
        if number[i:i+5] > max_seq:
            max_seq = number[i:i+5]
    return int(max_seq)
