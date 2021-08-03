def sequence_sum(begin_number, end_number, step):
    liste = []

    while begin_number <= end_number:
        liste.append(begin_number)
        begin_number = begin_number + step

    return sum(liste)
