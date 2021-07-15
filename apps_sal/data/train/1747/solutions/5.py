def crosstable(players, results):
    scores=[sum(x for x in result if x) for result in results]
    sb=[]
    for i,result in enumerate(results):
        s=0
        for j,w in enumerate(result):
            if w is None:
                continue
            s+=w*scores[j]
        sb.append(s)
    rank=sorted(list(range(len(players))),key=lambda x:(-scores[x],-sb[x],players[x].split(' ')[1]))
    no_len=len(str(len(players)))
    name_len=max(len(p) for p in players)
    score_len=max(len('{:.1f}'.format(s)) for s in scores)
    sb_len=max(len('{:.2f}'.format(s)) for s in sb)
    r=[]
    title='#'.rjust(no_len)+'  '+'Player'.ljust(name_len)+'  '
    for i in range(1,len(players)+1):
        title+=str(i).rjust(no_len)+' '
    bar='='*len(title)
    header_sb='SB'.center(sb_len)
    if sb_len%2==1:
        header_sb=header_sb[1:]+' '
    title+=' '+'Pts'.center(score_len)+'  '+header_sb
    bar+='='*(score_len+sb_len+3)
    r.append(title.rstrip())
    r.append(bar)
    prev_sb=None
    for i,j in enumerate(rank):
        if prev_sb and prev_sb==(scores[j],sb[j]):
            no=' '
        else:
            no=str(i+1)
        line=no.rjust(no_len)+'  '+players[j].ljust(name_len)+'  '+' '*(no_len-1)
        mat=[]
        for k in rank:
            if j==k:
                mat.append(' ')
            else:
                mat.append({0:'0',0.5:'=',1:'1'}[results[j][k]])
        space=' '*no_len
        line+=space.join(mat)+'  '
        score_j='{:.1f}'.format(scores[j])
        sb_j='{:.2f}'.format(sb[j])
        line+=score_j.rjust(score_len)+'  '+sb_j.rjust(sb_len)
        prev_sb=(scores[j],sb[j])
        r.append(line)
    return '\n'.join(r)
