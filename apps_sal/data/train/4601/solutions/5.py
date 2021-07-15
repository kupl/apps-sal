from math import ceil, log

def mormons(n, r, target):
    return ceil(log(target/n, r+1))

