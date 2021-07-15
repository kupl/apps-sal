def scratch(lottery):
    return sum(int(combi.split()[-1]) for combi in lottery if combi.split()[0]==combi.split()[1]==combi.split()[2]) or 0
