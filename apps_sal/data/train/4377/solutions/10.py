def solve(a, b):
    table_score = {'Player1': 0, 'Player2': 0}
    for (i, s) in enumerate(a):
        if s > b[i]:
            table_score['Player1'] += 1
        if s < b[i]:
            table_score['Player2'] += 1
    if table_score['Player1'] == table_score['Player2']:
        return '{0}, {1}: that looks like a "draw"! Rock on!'.format(table_score['Player1'], table_score['Player2'])
    if table_score['Player1'] > table_score['Player2']:
        return '{0}, {1}: Alice made "Kurt" proud!'.format(table_score['Player1'], table_score['Player2'])
    if table_score['Player1'] < table_score['Player2']:
        return '{0}, {1}: Bob made "Jeff" proud!'.format(table_score['Player1'], table_score['Player2'])
