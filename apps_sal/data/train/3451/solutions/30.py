def triangle(row):
    return row[0] if len(row) == 1 else triangle(['BGR'.replace(l1, '').replace(l2, '') if l1 != l2 else l1 for l1, l2 in zip(row,row[1:])])
    

