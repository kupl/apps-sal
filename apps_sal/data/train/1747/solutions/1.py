def transform(ch):
    s = ''
    for car in ch:
        car1 = car
        if 'A' <= car <= 'Z': car1 = chr(ord('Z')-ord(car)+ord('A'))
        if 'a' <= car <= 'z': car1 = chr(ord('z')-ord(car)+ord('a'))
        s += car1
    return s
        
def crosstable(players, results):
    scores = [sum([sc for sc in line if not sc is None]) for line in results]
    sb = [sum([scores[i] if results[j][i] == 1 \
                        else scores[i]/2 if results[j][i] == 0.5 \
                        else 0 \
                        for i in range(len(results)) if not results[j][i] is None]) \
                        for j in range(len(results))]
    rank = [sum([1 if (scores[j] > scores[i]) or (scores[i] == scores[j] and sb[j] > sb[i])\
                   else 0 \
                   for j in range(len(scores))])+1 for i in range(len(scores))]
    res = list(zip(scores, 
                  sb, 
                  [transform(player.split()[1]) for player in players], 
                  range(len(results))))
    #print(res)
    res.sort(reverse=True)
    #print(rank, res)
    ranksize = max([len(str(r)) for r in rank])
    namesize = max([len(name) for name in players])
    ptssize = max([len('%0.1f' % (score,)) for score in scores])
    SBsize = max([len('%0.2f' % (sbs,)) for sbs in sb])
    
    scdetails = [' '.join([(' ' if results[pl[3]][pl1[3]] is None \
         else '=' if results[pl[3]][pl1[3]] == 0.5 \
         else '1' if results[pl[3]][pl1[3]] == 1 \
         else '0').rjust(ranksize) for pl1 in res]) for pl in res]
    
    resultat = [
        '  '.join(['#'.rjust(ranksize), 
         'Player'.ljust(namesize),
         ' '.join([str(i).rjust(ranksize) for i in range(1, len(players) + 1)]),
         'Pts'.ljust(ptssize),
         'SB'.rjust(2+(SBsize-2)//2)
        ])
    ]
    for i in range(len(res)):
        pl = res[i]
        ll = [(str(rank[pl[3]]) if i == 0 or rank[pl[3]] != rank[res[i-1][3]] \
                               else ' ').rjust(ranksize),
              players[pl[3]].ljust(namesize),
              scdetails[i],
              ('%0.1f' % (pl[0],)).rjust(ptssize),
              ('%0.2f' % (pl[1],)).rjust(SBsize)]
        ll = '  '.join(ll)
        if i == 0: resultat.append('=' * len(ll))
        resultat.append(ll)
    return '\n'.join(resultat)
