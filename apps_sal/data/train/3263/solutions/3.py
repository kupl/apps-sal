def solve(arr):
    k = sorted((int(x[:2]) * 60 + int(x[3:]) for x in arr))
    z = [(k[i] - k[i - 1]) % 1440 for i in range(len(k))]
    return len(k) > 1 and '{:02}:{:02}'.format(*divmod(max(z) - 1, 60)) or '23:59'
