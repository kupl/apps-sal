from numpy import mean


def find_average(N):
    return 0 if len(N) < 1 else mean(N)
