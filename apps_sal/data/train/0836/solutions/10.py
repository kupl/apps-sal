def find_movie(T, R):
    e = []
    for d in range(len(T)):
        f = []
        f.append(int(T[d]) * int(R[d]))
        f.append(int(R[d]))
        f.append(int(T[d]))
        e.append(f)
    max_val = []
    max_val = max(e)
    index = e.index(max_val)
    return (index + 1)


t = int(input())
for x in range(t):
    n = int(input())
    timing = []
    timing = str(input())
    timing = timing.split()
    rating = []
    rating = str(input())
    rating = rating.split()
    index = find_movie(timing, rating)
    print(index)
