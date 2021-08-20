def outed(meet, boss):
    return 'Nice Work Champ!' if sum(meet.values()) + meet[boss] > 5 * len(meet) else 'Get Out Now!'
