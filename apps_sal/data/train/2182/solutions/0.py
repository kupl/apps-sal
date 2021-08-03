oleg = input()
igor = input()
oleg = sorted(list(oleg))
igor = sorted(list(igor))
n = len(oleg)
oleg_turns = (n + 1) // 2
igor_turns = n // 2
min_oleg_id = 0
min_igor_id = n - igor_turns
ans = ['?'] * n
max_oleg_id = oleg_turns - 1
max_igor_id = n - 1
curr_turn = 'o'
next_turn = {'o': 'i', 'i': 'o'}
l_ans = 0
r_ans = n - 1
while r_ans >= l_ans:
    if curr_turn == 'o':
        if oleg[min_oleg_id] < igor[max_igor_id]:
            ans[l_ans] = oleg[min_oleg_id]
            l_ans += 1
            min_oleg_id += 1
        else:
            ans[r_ans] = oleg[max_oleg_id]
            r_ans += -1
            max_oleg_id += -1
        curr_turn = 'i'
    else:
        if igor[max_igor_id] > oleg[min_oleg_id]:
            ans[l_ans] = igor[max_igor_id]
            l_ans += 1
            max_igor_id += -1
        else:
            ans[r_ans] = igor[min_igor_id]
            r_ans += -1
            min_igor_id += 1
        curr_turn = 'o'
strans = ''.join(ans)
print(strans)
