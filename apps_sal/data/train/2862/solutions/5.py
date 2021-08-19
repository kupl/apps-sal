def leaderboard_climb(scores, kara):
    answer = []
    kara = kara[::-1]
    (rank, iScore, lastScore) = (1, 0, scores[0])
    l = len(scores)
    for karaScore in kara:
        while True:
            if karaScore >= lastScore or iScore >= l:
                answer.append(rank)
                break
            iScore += 1
            if iScore < l:
                score = scores[iScore]
                if lastScore != score:
                    lastScore = score
                    rank += 1
            else:
                rank += 1
    return answer[::-1]
