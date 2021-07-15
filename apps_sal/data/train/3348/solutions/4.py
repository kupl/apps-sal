def outed(meet, boss):
    return 'Get Out Now!' if sum([ i[1] for i in list(meet.items())] + [meet[boss]])/len(meet) <= 5 else 'Nice Work Champ!'

