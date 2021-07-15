def scratch(lottery):
    return sum(int(i.split()[-1]) for i in lottery if len(set(i.split()))==2)
