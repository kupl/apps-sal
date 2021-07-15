
def queue_battle(dist,*armies):

    armies_copy = [*armies]
    armies= [[*a] for a in armies]
    armies_left = [i for i in range(len(armies))]
    soldiers_id = [[i for i in range(len(army))] for army in armies]
    bullets_between = [[] for i in armies_left]

    while True:

        bullets_between = [[[s, s+l] for (s, l) in bullets] for bullets in bullets_between]
        recovering_armies = []

        for i in range(len(bullets_between)):
            for j in range(len(bullets_between[i])):
                if bullets_between[i][j][1] >= dist:
                    del armies[armies_left[(i+1)%len(armies_left)]][0]
                    del soldiers_id[armies_left[(i+1)%len(armies_left)]][0]
                    recovering_armies.append(armies_left[(i+1)%len(armies_left)])
                    break
            bullets= []
            for j in range(len(bullets_between[i])):
                if bullets_between[i][j][1] < dist:
                    bullets.append(bullets_between[i][j])
            bullets_between[i] = bullets

        for i in range(len(armies_left)):
            if armies_left[i] not in recovering_armies:
                bullet_speed = armies[armies_left[i]][0]
                bullets_between[i].append( [bullet_speed, 0] )

        if len(armies_left) == 0: 
            return (-1, ())
        if len(armies_left) == 1:
            return (armies_left[0], tuple(soldiers_id[armies_left[0]]))

        for i in range(len(armies_left)):
            if armies_left[i] not in recovering_armies:
                soldiers_id[armies_left[i]].append(soldiers_id[armies_left[i]].pop(0))
                armies[armies_left[i]].append(armies[armies_left[i]].pop(0))

        armies_left_new = [*armies_left]
        for i in range(len(armies_left)):
            if len(armies[armies_left[i]]) == 0:
                armies_left_new.remove(armies_left[i])
                bullets_between = [[] for i in armies_left_new]

        armies_left = armies_left_new

    return 
