def max_score(storage):
    """Returns the max score for the given storage array"""
    s = len(storage)
    counts = {}
    for cookie in storage:
        if cookie in counts:
            counts[cookie] += 1
        else:
            counts[cookie] = 1

    while len(list(counts.keys())) >= 6:
        minimum = min(counts.values())
        s += 4 * minimum
        to_delete = []
        for cookie, count in list(counts.items()):
            counts[cookie] -= minimum
            if counts[cookie] == 0:
                to_delete.append(cookie)
        for key in to_delete:
            counts.pop(key)
    while len(list(counts.keys())) >= 5:
        minimum = min(counts.values())
        s += 2 * minimum
        to_delete = []
        for cookie, count in list(counts.items()):
            counts[cookie] -= minimum
            if counts[cookie] == 0:
                to_delete.append(cookie)
        for key in to_delete:
            counts.pop(key)
    while len(list(counts.keys())) >= 4:
        minimum = min(counts.values())
        s += 1 * minimum
        to_delete = []
        for cookie, count in list(counts.items()):
            counts[cookie] -= minimum
            if counts[cookie] == 0:
                to_delete.append(cookie)
        for key in to_delete:
            counts.pop(key)
    return s


T = int(input())
while T > 0:
    N = int(input())
    max_s = -1
    max_idx = 0
    tied = False
    for idx in range(N):
        row = list(map(int, input().split()))
        score = max_score(row[1:])
        if score > max_s:
            max_s = score
            max_idx = idx
            tied = False
        elif score == max_s:
            tied = True
    if tied:
        print('tie')
    elif max_idx == 0:
        print('chef')
    else:
        print(max_idx + 1)
    T -= 1
