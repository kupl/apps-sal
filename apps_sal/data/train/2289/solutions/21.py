A = '.' + input()
smallalphas = list(map(chr, list(range(ord('a'), ord('z') + 1))))
answers = {c: 0 for c in smallalphas}
last_ch = 'a'
history = []
for a in reversed(A):
    ch = 'a'
    for c in smallalphas:
        if answers[ch] > answers[c]:
            ch = c
    answers[a] = answers[ch] + 1
    history.append(ch)
history.reverse()
ans = [history[0]]
for (i, a) in enumerate(A):
    if ans[-1] == a:
        ans.append(history[i])
print(''.join(ans))
