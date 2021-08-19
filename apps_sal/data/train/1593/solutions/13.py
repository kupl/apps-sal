# cook your dish here
T = int(input())

avail = [100, 50, 10, 5, 2, 1]

for i in range(T):
    N = int(input())
    notes = []
    for note in avail:
        if note > N:
            continue
        else:
            c = N // note
            notes.append(c)
            N = N % note
    print(sum(notes))
