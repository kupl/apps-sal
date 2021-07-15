def outed(meet, boss):
    total = sum(v for v in meet.values()) + meet[boss]
    if total / len(meet) <= 5:
        return 'Get Out Now!'
    return 'Nice Work Champ!'
