# Will work for any size (as long as it's a square)
def is_magical(sq):
    N = int(len(sq)**0.5)
    res = sum(sq[::N+1])
    return res == sum(sq[N-1:-1:N-1]) and all(sum(sq[i*N:(i+1)*N]) == sum(sq[i::N]) == res for i in range(N))
