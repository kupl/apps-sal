outed=lambda meet, boss: "Get Out Now!" if sum([meet[i]*(1 if i!=boss else 2) for i in meet])/len(meet)<=5 else "Nice Work Champ!"
