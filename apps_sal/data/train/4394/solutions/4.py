"""
1.创建A,B两队的字典 key=player几号球员  value=被罚数 初始值都是0 黄牌+1 红牌+2
2.循环cards 先判断是A.B哪队？再判断是几号球员？ 再看是哪个颜色？
3.如果这个队员已经不再team中（淘汰） 则继续循环
4.若为黄色则通过key=player找到value+1 红色则+2
5.若value=2则del
6.如果删除后len(team)<7  跳出循环
7.最后返回len(A) len(B)---因为team=A 浅拷贝
注意：copy是深拷贝 B不会随着A改变而改变
"""


def men_still_standing(cards):
    A = {k: 0 for k in range(1, 12)}
    B = A.copy()
    for card in cards:
        team = A if card[0] == 'A' else B
        player = int(card[1:-1])
        color = card[-1]
        if player not in team:
            continue
        team[player] += 1 if color == 'Y' else 2
        if team[player] >= 2:
            del team[player]
        if len(team) < 7:
            break
    return (len(A), len(B))
