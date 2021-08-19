rounds = input()
rounds = int(rounds)
lead = 0
s1 = 0
s2 = 0
for i in range(rounds):
    scores = input()
    scores = scores.split()
    s1 += int(scores[0])
    s2 += int(scores[1])
    if s1 - s2 > lead:
        leader = 1
        lead = s1 - s2
    elif s2 - s1 > lead:
        leader = 2
        lead = s2 - s1
print(str(leader) + ' ' + str(lead))
