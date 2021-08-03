END = 9876543211


def get_sequence(offset, size):
    number = 1023456789
    sequence = []

    if offset < number:
        offset = number

    for element in range(offset, END):
        if check_number(element):
            sequence.append(element)

        if len(sequence) == size:
            break

    return sequence


def check_number(number):
    seq = set(str(number))

    return len(seq) == 10
