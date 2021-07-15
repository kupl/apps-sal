def asterisc_it(n_sequence: str) -> str:
    """ Insert an asterisk (*) between every pair of even digits. """
    _result = ""

    if type(n_sequence) is int:
        n_sequence = str(n_sequence)
    else:
        n_sequence = "".join(str(_) for _ in n_sequence)

    for ix, num in enumerate(n_sequence):
        if ix < len(n_sequence) - 1:
            if not int(num) % 2 and not int(n_sequence[ix+1]) % 2:
                _result += f"{num}*"
            else:
                _result += str(num)
        else:
            _result += str(num)

    return _result

