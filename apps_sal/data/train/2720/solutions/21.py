def solution(digits):
    number_string = str(digits)

    sequence_list = []

    for i in range(len(number_string) - 4):

        five_sequence = number_string[i:i + 5]

        if int(five_sequence) > int(number_string[i + 1:i + 6]):
            sequence_list.append(int(five_sequence))

    return max(sequence_list)
