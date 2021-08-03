t = int(input().strip())
for i in range(t):
    R, C = list(map(int, input().strip().split()))
    hit = [''] * R
    for j in range(R):
        hit[j] = input().strip().lower()
    found = False
    for w in hit:
        if w.find('spoon') != -1:
            print('There is a spoon!')
            found = True
            break
    if not found:
        for i in range(C):
            new = ''.join([x[i] for x in hit])
            if new.find('spoon') != -1:
                print('There is a spoon!')
                found = True
                break
        if not found:
            print('There is indeed no spoon!')
