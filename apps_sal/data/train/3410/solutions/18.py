def scratch(lottery):
    return sum((int(i.split()[3]) for i in lottery if i.split()[0] == i.split()[1] == i.split()[2]))
