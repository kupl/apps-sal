def outed(meet, boss):
    # sum of all people plus boss value, boss counts twice
    total_score = sum(meet.values()) + meet[boss]
    happiness_rating = total_score / len(meet)
    if happiness_rating > 5:
        return 'Nice Work Champ!'
    else:
        return 'Get Out Now!'
