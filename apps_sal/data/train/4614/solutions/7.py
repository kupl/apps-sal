def scoreboard(who_ate_what):
    score_board = []
    for person in who_ate_what:
        score = person.get('chickenwings',0)*5 + person.get('hamburgers',0)*3 + person.get('hotdogs',0)*2       
        contestant = {x:person[x] for x in ['name']}
        contestant.update({'score':score})        
        score_board.append(contestant )            
    return sorted(score_board, key=lambda k: (-k['score'], k['name']))
