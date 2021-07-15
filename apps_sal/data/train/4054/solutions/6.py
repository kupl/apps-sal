def scoring(array):
    scores = []
    output = []
    
    for ply in array:
        score = (ply['norm_kill'] * 100) + (ply['assist'] * 50) + (ply['damage'] * 0.50) + ply['healing'] + (2 ** ply['streak']) + (ply['env_kill'] * 500)
        scores.append((ply['name'], score))
    
    def getScore(tup):
        return tup[1]
    
    players = sorted(scores, key=getScore, reverse=True)

    for player in players:
        output.append(player[0])
        
    return output
