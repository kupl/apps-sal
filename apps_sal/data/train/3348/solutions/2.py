def outed(meet, boss):
    return 'Get Out Now!' if sum((meet[person] if not person == boss else meet[person] * 2 for person in meet)) / len(meet) <= 5 else 'Nice Work Champ!'
