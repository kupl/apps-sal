def shortest_time(n,m,speeds):
    return min([speeds[3]*(n-1),(abs(m-n)+n-1)*speeds[0]+2*speeds[1]+speeds[2]])
