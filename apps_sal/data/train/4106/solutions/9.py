def self_converge(number, z=0, counter=0, previous=[]):
    return (lambda sol: -1 if sol == 0 else counter if number in previous else self_converge(sol, len(str(number)) if z == 0 else z, counter + 1, previous + [number]))((lambda n: int(''.join(sorted(n, reverse=True))) - int(''.join(sorted(n))))(str(number).zfill(z)))
