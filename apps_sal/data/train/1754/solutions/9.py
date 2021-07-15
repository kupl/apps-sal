def valid(a):
    groups_per_day = len(a[0])
    all_groups = [set(x) for x in a[0]]
    golfers = ''.join(a[0])
    for day in a[1:]:
        if len(day) != groups_per_day: return False
        if set(''.join(day)) != set(golfers): return False 
        for group in day:
            if [1 for g in all_groups if len(g & set(group))>1]: return False
            all_groups.append(set(group))
    return True

