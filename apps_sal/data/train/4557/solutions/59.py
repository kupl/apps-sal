def row_weights(a):
    return (sum([x[1] for x in enumerate(a) if x[0]%2==0]),
            sum([x[1] for x in enumerate(a) if x[0]%2!=0]))
