def expanded_form(num):
    xs = str(num).split('.')
    return ' + '.join(
        [f'{x}{"0" * i}' for i, x in enumerate(xs[0][::-1]) if x != '0'][::-1]
        + [f'{x}/{10 ** i}' for i, x in enumerate(xs[1], 1) if x != '0']
    )
