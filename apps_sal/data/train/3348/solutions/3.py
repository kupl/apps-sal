def outed(meet, boss):
    total = sum(v if k != boss else v * 2 for k, v in meet.items())
    return 'Nice Work Champ!' if total / len(meet) > 5 else 'Get Out Now!'
