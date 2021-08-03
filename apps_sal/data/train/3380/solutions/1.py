def look_and_say_sequence(first, n):
    result = first

    for _ in range(n - 1):

        sequence = result
        result = ''
        index = 0

        while index < len(sequence):

            pending = sequence[index]
            count = 0

            while index < len(sequence) and pending == sequence[index]:
                count += 1
                index += 1

            result += "{}{}".format(count, pending)

    return result
