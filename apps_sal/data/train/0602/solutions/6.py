lyrics = list(map(str, input().rstrip().split(" ")))
mini1 = lyrics[0]
for i in lyrics:
    if len(i) < len(mini1):
        mini1 = i
t = 0
remix = []
while True:
    try:
        remix.append(mini1)
        remix.append(lyrics[t])
        t+=1
    except IndexError:
        break
print(" ".join(remix), end="")
