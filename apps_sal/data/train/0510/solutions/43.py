
import bisect

N = int(input())
S = input()
Q = int(input())

# 現時点でどこに何があるか
cS = [""] * N
# ある文字の位置
char_idxs = [[]for _  in range(26)]

# i番目は文字s、を保存
for i,s in enumerate(S):
    cS[i] = s
    char_idxs[ord(s) - 97].append(i)

query = [tuple(map(str, input().split())) for _ in range(Q)]




for q,a,b in query:
    
    # q == 1の時、a番目の文字をbに置き換え
    if q == "1":
        # 現時点の文字と置き換え後が同じなら何もしない
        if cS[int(a) - 1] == b:
            continue
        else:
            #print("---", char_idxs[ord(cS[]) - 97], int(a)-1, bisect.bisect_right(char_idxs[ord(b) - 97], int(a)-1))
            # a番目の文字を書き換える

            
            idx = bisect.bisect_right(char_idxs[ord(cS[int(a)-1]) - 97], int(a)-1)
            # idxの左の値がa番目であれば、それを消す
            if char_idxs[ord(cS[int(a)-1]) - 97][idx-1] == int(a)-1:
                # delの方が早いか？
                char_idxs[ord(cS[int(a)-1]) - 97][idx-1:idx] = []
            
            # bの文字がa番目にあるよ、を保存
            bisect.insort_right(char_idxs[ord(b) - 97], int(a) - 1)

            # 置き換え
            cS[int(a) - 1] = b

    # q == 2の時、範囲の文字種の個数を調べる
    else:
        cnt = 0
        for i in range(26):
            # そもそもその文字が文字列全体になければ考えない
            if len(char_idxs[i]) == 0: continue
            # bisect_leftで a-1 を入れられる場所を探して、その時に右にある値がb-1以下であれば含まれる
            l = bisect.bisect_left(char_idxs[i], int(a)-1)
            #r = bisect.bisect_right(char_idxs[i], int(b)-1)

            # char_idxs[i][l]はa-1より右に文字種iが初めて出てくる位置なので、それがb-1を含む右側にあればOK
            if l < len(char_idxs[i]) and char_idxs[i][l] <= int(b)-1:
                cnt += 1

        print(cnt)



