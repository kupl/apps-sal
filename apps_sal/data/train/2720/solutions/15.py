def solution(d):
    for x in '9876543210':
        for y in '9876543210':
            for z in '9876543210':
                for w in '9876543210':
                    for q in '9876543210':
                        if d.find(x + y + z + w + q) != -1:
                            return int(x + y + z + w + q)
