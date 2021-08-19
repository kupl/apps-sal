def score_pole_vault(vaulter_list):
    i = j = 0
    retDict = {}
    vaulter = {}
    updatedVaulterList = []
    for vaulter_dict in vaulter_list:
        vaulter = {'name': vaulter_dict['name'], 'results': vaulter_dict['results']}
        highestVaulterJump = 0
        totalUnsuccessfulAttempts = 0
        unsuccessfulAttemptsAtHighestJump = 0
        j = 0
        for resultsList in vaulter_list[i]['results']:
            j -= 1
            if 'O' in resultsList:
                highestVaulterJump = j
                unsuccessfulAttemptsAtHighestJump = resultsList.count('X')
            totalUnsuccessfulAttempts += resultsList.count('X')
        vaulter['highestSuccessfulJump'] = highestVaulterJump
        vaulter['numOfUnsuccessfulAttemptsAtHighestSuccessfulJump'] = unsuccessfulAttemptsAtHighestJump
        vaulter['numOfTotalUnsuccessfulAttempts'] = totalUnsuccessfulAttempts
        updatedVaulterList.append(dict(vaulter))
        i += 1
    updatedVaulterList = sorted(updatedVaulterList, key=lambda i: (i['highestSuccessfulJump'], i['numOfUnsuccessfulAttemptsAtHighestSuccessfulJump'], i['numOfTotalUnsuccessfulAttempts'], i['name']))
    jumpOff = 0
    positionsAssigned = 0
    for i in range(len(updatedVaulterList)):
        if i == 0:
            retDict['1st'] = updatedVaulterList[i]['name']
            positionsAssigned += 1
        if i > 0:
            if updatedVaulterList[i]['highestSuccessfulJump'] == updatedVaulterList[0]['highestSuccessfulJump']:
                if updatedVaulterList[i]['numOfUnsuccessfulAttemptsAtHighestSuccessfulJump'] == updatedVaulterList[0]['numOfUnsuccessfulAttemptsAtHighestSuccessfulJump']:
                    if updatedVaulterList[i]['numOfTotalUnsuccessfulAttempts'] == updatedVaulterList[0]['numOfTotalUnsuccessfulAttempts']:
                        retDict['1st'] = retDict['1st'] + ', ' + updatedVaulterList[i]['name']
                        jumpOff = 1
                        positionsAssigned += 1
    if jumpOff:
        retDict['1st'] = retDict['1st'] + ' (jump-off)'
    tie = 0
    if positionsAssigned == 1:
        for i in range(1, len(updatedVaulterList)):
            if i == 1:
                retDict['2nd'] = updatedVaulterList[i]['name']
                positionsAssigned += 1
            if i > 1:
                if updatedVaulterList[i]['highestSuccessfulJump'] == updatedVaulterList[1]['highestSuccessfulJump']:
                    if updatedVaulterList[i]['numOfUnsuccessfulAttemptsAtHighestSuccessfulJump'] == updatedVaulterList[1]['numOfUnsuccessfulAttemptsAtHighestSuccessfulJump']:
                        if updatedVaulterList[i]['numOfTotalUnsuccessfulAttempts'] == updatedVaulterList[1]['numOfTotalUnsuccessfulAttempts']:
                            retDict['2nd'] = retDict['2nd'] + ', ' + updatedVaulterList[i]['name']
                            tie = 1
                            positionsAssigned += 1
    if tie:
        retDict['2nd'] = retDict['2nd'] + ' (tie)'
    tie = 0
    if positionsAssigned == 2:
        for i in range(2, len(updatedVaulterList)):
            if i == 2:
                retDict['3rd'] = updatedVaulterList[i]['name']
                positionsAssigned += 1
            if i > 2:
                if updatedVaulterList[i]['highestSuccessfulJump'] == updatedVaulterList[2]['highestSuccessfulJump']:
                    if updatedVaulterList[i]['numOfUnsuccessfulAttemptsAtHighestSuccessfulJump'] == updatedVaulterList[2]['numOfUnsuccessfulAttemptsAtHighestSuccessfulJump']:
                        if updatedVaulterList[i]['numOfTotalUnsuccessfulAttempts'] == updatedVaulterList[2]['numOfTotalUnsuccessfulAttempts']:
                            retDict['3rd'] = retDict['3rd'] + ', ' + updatedVaulterList[i]['name']
                            tie = 1
                            positionsAssigned += 1
    if tie:
        retDict['3rd'] = retDict['3rd'] + ' (tie)'
    return retDict
