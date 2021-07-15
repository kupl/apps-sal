def evil_code_medal(user_time, gold, silver, bronze):
    return ['None', 'Bronze', 'Silver', 'Gold'][
        (user_time < bronze) + (user_time < silver) + (user_time < gold)
    ]
