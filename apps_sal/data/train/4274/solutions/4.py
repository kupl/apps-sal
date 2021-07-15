def do_math(s) :
  xs = [x for x, _ in sorted([(int(''.join(c for c in x if c.isdigit())), next(c for c in x if c.isalpha())) for x in s.split()], key = lambda x: x[1])]
  return round(eval('(' * len(xs) + ''.join(f'{x}){op}' for x, op in zip(xs, '+-*/+-*/+-*/+-*/+-*/+-*/+-'))[:-1]))
