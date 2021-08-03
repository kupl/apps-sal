SI = {'ms': .001, 's': 1, 'm': 60, 'h': 60 * 60}
def convert_SI(val, unit_from, unit_to): return val * SI[unit_from] / SI[unit_to]


convert_ms = __import__('functools').partial(convert_SI, unit_to='ms')
past = lambda *args: sum(convert_ms(val, unit) for val, unit in zip(args, 'hms'))
