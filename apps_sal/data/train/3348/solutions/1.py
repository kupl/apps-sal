def outed(meet, boss):
    total_score = sum(meet.values()) + meet[boss]
    happiness_rating = total_score / len(meet)
    if happiness_rating > 5:
        return 'Nice Work Champ!'
    else:
        return 'Get Out Now!'
