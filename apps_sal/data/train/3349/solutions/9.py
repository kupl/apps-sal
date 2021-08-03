def find_missing_number(sequence):

    sequence = sequence.strip().split()

    data = []

    for ch in sequence:
        if not ch.isdigit():
            return 1
        else:
            data.append(int(ch))

    if data == []:
        return 0
    else:
        data = sorted(data)

    pattern = list(range(1, len(data) + 1))

    if pattern == data:
        return 0                   # all is good
    else:
        for pair in zip(pattern, data):
            if pair[0] != pair[1]:
                return pair[0]        # here's the missing number
