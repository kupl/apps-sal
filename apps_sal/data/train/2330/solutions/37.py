S = input()
N = len(S)

# 1-originにする
# S[0]があるとすると、0,Nに別れることはないので、0
S = "0" + S

# 葉できった時に、1_(n-1)になるはず
if S[1] != "1":
    print("-1")
    return

# 0_Nに別れることはない
if S[-1] != "0":
    print("-1")
    return

# S[i]=1の時,i_(N-i)に別れる-> S[i]==S[N-i]
for s, rev_s in zip(S, reversed(S)):
    if s != rev_s:
        print("-1")
        return

prev = N
for i in reversed(list(range(1, N))):
    print((i, prev))
    # これまでに、N-i個がすでに気に追加されている。prevとcur(i)の間できると、(i_N-i)に別れる
    if S[i] == "1":
        prev = i
    else:
        # 葉になる(1_N-1)に別れるため、i_(N-i)にはならない。S[1]=S[N-1]=1は決まっている。
        pass
