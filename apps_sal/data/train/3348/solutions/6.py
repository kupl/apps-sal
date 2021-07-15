def outed(meet, boss):
    return 'Nice Work Champ!' if (sum(meet.values()) + meet[boss]) / len(meet) > 5 else 'Get Out Now!'
