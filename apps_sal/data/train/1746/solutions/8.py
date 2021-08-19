only_show_wrong()


def rpg(field, actions):
    newfield = [[val for val in row] for row in field]
    playerpos = [0, 0, 0]  # [x,y,dir]
    playerstats = [3, 1, 1, 0]  # Health, attack, defense, enemies killed
    playerbag = []
    myactions = actions

    # Board stuff
    demonlord_hp = [10]
    merchants = []  # [[posx,posy,coinsgiven][posx,posy,coinsgiven]] this list holds a 'reference' to all merchants

    # Finding player position
    for row in newfield:
        for val in row:
            if val == '^':
                playerpos[0] = row.index(val)
                playerpos[1] = newfield.index(row)
                playerpos[2] = 0
            elif val == '>':
                playerpos[0] = row.index(val)
                playerpos[1] = newfield.index(row)
                playerpos[2] = 1
            elif val == 'v':
                playerpos[0] = row.index(val)
                playerpos[1] = newfield.index(row)
                playerpos[2] = 2
            elif val == '<':
                playerpos[0] = row.index(val)
                playerpos[1] = newfield.index(row)
                playerpos[2] = 3
            elif val == 'M':
                merchants.append([row.index(val), newfield.index(row), 3])
    # Taking the actions
    for action in myactions:
        # Save players last known position for damage calculation
        lastplayerpos = playerpos[:]
        legalmove = True
        if(action == 'F'):
            legalmove = forward(newfield, playerpos, playerbag, playerstats)
        elif(action == '^'):
            playerpos[2] = 0
            newfield[playerpos[1]][playerpos[0]] = getplayerstring(playerpos)
        elif (action == '>'):
            playerpos[2] = 1
            newfield[playerpos[1]][playerpos[0]] = getplayerstring(playerpos)
        elif (action == 'v'):
            playerpos[2] = 2
            newfield[playerpos[1]][playerpos[0]] = getplayerstring(playerpos)
        elif (action == '<'):
            playerpos[2] = 3
            newfield[playerpos[1]][playerpos[0]] = getplayerstring(playerpos)
        elif (action == 'A'):
            legalmove = attack(newfield, playerpos, playerstats, demonlord_hp)
            if(legalmove == 'win'):
                print('we won!')
                break
        elif (action == 'C'):
            legalmove = coin(newfield, playerpos, playerbag, merchants)
        elif (action == 'K'):
            legalmove = key(newfield, playerpos, playerbag)
        elif (action == 'H'):
            legalmove = health(playerbag, playerstats)

        if(legalmove == False):
            print("Encountered invalid!")
            print("last action: " + action)
            return None

        # Check for enemy damage and shit
        enemies = getajanba(newfield, lastplayerpos)
        if(len(enemies) > 0):
            print("Printing enemies!")
            print('last action: ' + action)
            for enemy in enemies:
                print(enemy)
        for enemy in enemies:
            damagetodeal = max(0, 2 - playerstats[2]) if enemy == 'E' else max(0, 3 - playerstats[2])
            playerstats[0] -= damagetodeal
            if(playerstats[0] <= 0):
                return None

    # Actions finished, give back output
    sortedbag = playerbag if len(playerbag) <= 1 else sorted(playerbag)
    return (newfield, playerstats[0], playerstats[1], playerstats[2], sortedbag)


def forward(field, playerpos, bag, playerstats):
    # find where the in front of the player is
    # check_movement returns [obj, posx, posy]
    infront = check_front(field, playerpos)

    if(infront == False):  # if oob
        return False

    obj = infront[0]
    posx = infront[1]
    posy = infront[2]
    if(obj == '#' or obj == 'M' or obj == '-' or obj == '|' or obj == 'E' or obj == 'D'):
        return False
    elif(obj == 'C' or obj == 'K' or obj == 'H'):  # Time to check for objects(inventory)
        bag.append(obj)
        print("obtained: " + obj + "   bag is now: ")
        print(bag)
        field[posy][posx] = ' '
    elif(obj == 'S'):
        playerstats[2] += 1
        field[posy][posx] = ' '
    elif(obj == 'X'):
        playerstats[1] += 1
        field[posy][posx] = ' '
    # Update player pos
    field[playerpos[1]][playerpos[0]] = ' '
    field[posy][posx] = getplayerstring(playerpos)
    playerpos[0] = posx
    playerpos[1] = posy
    return True


def attack(field, playerpos, playerstats, demonlord):
    infront = check_front(field, playerpos)
    if(infront == False):
        return False
    enemy = infront[0]
    posx = infront[1]
    posy = infront[2]

    if enemy == 'E':
        field[posy][posx] = ' '
        playerstats[3] += 1
        if playerstats[3] >= 3:
            playerstats[1] += 1
            playerstats[3] = 0
        return True
    elif enemy == 'D':
        demonlord[0] -= playerstats[1]
        if demonlord[0] <= 0:
            field[posy][posx] = ' '
            return 'win'
    else:
        return False


def coin(field, playerpos, playerbag, merchants):
    # Do we have coins?
    if 'C' not in playerbag:
        return False

    # Is a merchant in front of us
    infront = check_front(field, playerpos)
    if(infront == False):
        return False
    obj = infront[0]
    posx = infront[1]
    posy = infront[2]
    if obj != 'M':
        print('No merchant in front!')
        return False
    # Find specific merchant in array
    for merchant in merchants:
        if merchant[0] == posx and merchant[1] == posy:
            playerbag.remove('C')
            merchant[2] -= 1
            print('giving coin to merchant')
            if merchant[2] <= 0:
                field[posy][posx] = ' '
                print('merchant should b gone')
            break
    return True


def key(field, playerpos, playerbag):
    # Do we have keys
    if 'K' not in playerbag:
        return False

    # Is a door in front of us
    infront = check_front(field, playerpos)
    if(infront == False):
        return False
    obj = infront[0]
    posx = infront[1]
    posy = infront[2]
    if obj != '-' and obj != '|':
        return False
    field[posy][posx] = ' '
    playerbag.remove('K')
    return True


def health(playerbag, playerstats):
    if playerstats[0] >= 3:
        return False
    if 'H' not in playerbag:
        return False
    playerstats[0] = 3
    playerbag.remove('H')
    return True


def check_front(field, playerpos):
    # checking direction of movement and get square
    posx = playerpos[0]
    posy = playerpos[1]
    posdir = playerpos[2]
    if(posdir == 0):
        posx += 0
        posy -= 1
    elif(posdir == 1):
        posx += 1
        posy -= 0
    elif(posdir == 2):
        posx += 0
        posy += 1
    elif(posdir == 3):
        posx -= 1
        posy -= 0

    # Check for OOB
    if (posx < 0 or posx >= len(field[0])) or (posy < 0 or posy >= len(field)):
        return False
    # Check for Objects
    obj = field[posy][posx]
    return [obj, posx, posy]


def getplayerstring(playerpos):
    if(playerpos[2] == 0):
        return '^'
    elif(playerpos[2] == 1):
        return '>'
    elif(playerpos[2] == 2):
        return 'v'
    elif(playerpos[2] == 3):
        return '<'


def getajanba(field, playerpos):
    enemylist = []
    tocheck = [[playerpos[0] + 1, playerpos[1]], [playerpos[0] - 1, playerpos[1]], [playerpos[0], playerpos[1] + 1], [playerpos[0], playerpos[1] - 1]]
    for check in tocheck:
        posx = check[0]
        posy = check[1]
        if (posx < 0 or posx >= len(field[0])) or (posy < 0 or posy >= len(field)):
            continue

        obj = field[posy][posx]
        if obj == 'E' or obj == 'D':
            enemylist.append(obj)
    return enemylist
