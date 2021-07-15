def scratch(lottery):
    return sum(int(s.split()[-1]) for s in lottery if len(set(s.split()[:-1])) == 1)
