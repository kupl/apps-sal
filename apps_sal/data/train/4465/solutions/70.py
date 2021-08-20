def super_size(n):
    sorted_integers = sorted(str(n), reverse=True)
    supersized_n = int(''.join(sorted_integers))
    return supersized_n
