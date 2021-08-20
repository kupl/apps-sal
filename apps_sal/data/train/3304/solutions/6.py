def is_inertial(a):
    try:
        return max(a) % 2 == 0 and min((e for e in a if e % 2)) > max((e for e in a if e % 2 == 0 and e < max(a)))
    except ValueError:
        return False
