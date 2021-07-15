
# A small class to represent a battalion
class Battalion:
    def __init__(self, position, soldiers, hit):
        self.position = position
        self.soldiers = soldiers
        self.hit = hit


def queue_battle(dist, *armies):
    #list of bullets currency on the air
    bullets = []
    #converting tuple of tuples to list of lists containing tuples with each soldier and his original position
    armies = [list((s, i) for i, s in enumerate(a)) for a in armies]
    #creating a list of battalions to keep track of things
    battalions = [Battalion(i, list(a), False) for i, a in enumerate(armies)]

    #Run the loop until one or less battalions remain
    while len(battalions) > 1:
        #Check for any hits this round, in reverse order to allow removing of items inside loop
        for b in reversed(bullets):
            target = battalions[b[2]]
            #Increase bullet distance by speed
            b[0] = b[0] + b[1][0]
            #Check if bullet reached the destination
            if b[0] >= dist:
                if not target.hit:
                    #remove the front soldier of the queue hit, but only if queue wasn't already hit this round
                    target.soldiers.pop(0)
                    #Set hit to true to avoid further hits this round
                    target.hit = True
                #Remove bullet that hit target    
                bullets.remove(b)

        #A helper variable to track any eliminations
        elim = 0
        #Loop through battalions, in reverse order as well to allow elimination
        for idx, ba in enumerate(reversed(battalions)):
            #Remove battalion with no soldiers left, remove all bullets as there will be a position change
            if not ba.soldiers:
                battalions.remove(ba)
                bullets = []
                elim += 1
            elif not ba.hit:
                if elim == 0:
                    #Reverse looping, so index 0 is really last, so should target battal
                    if idx == 0:
                        target = 0
                    else:
                        target = len(battalions) - idx
                        if target >= len(battalions):
                            target = 0
                    #Shoot a new bullet with distance, speed and target battalion index
                    bullets.append([0, ba.soldiers[0], target])
                #Switch the current shooter to the back of the queue
                ba.soldiers.insert(len(ba.soldiers), ba.soldiers[0])
                ba.soldiers.pop(0)
            ba.hit = False
    if battalions:
        pos = battalions[0].position
        survivors = tuple([s[1] for s in battalions[0].soldiers])
        return (pos,survivors)
    else:
        return (-1,())


