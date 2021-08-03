# cook your dish here
seq = list(map(float, input().split()))
for i in range(1, len(seq), 2):
    print("%.2f" % round(seq[i] * 10**int(seq[i + 1]), 2))
