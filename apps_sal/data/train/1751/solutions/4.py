def queue_battle(dist,*armies):
    
    #declare variables
    DIST = dist
    ARMY_COUNT = len(armies)
    
    #Keep track of active armies - needed for reassigning targets
    active_armies = []
    for army in range (0,ARMY_COUNT):
        active_armies.append(army)
    
    #Add each army and target to dictionary
    queues = {}
    for n, army in enumerate(armies):
        if n==len(armies)-1:
            target = 0
        else:
            target = n+1
        queues[n]={'target':target,'army':{k:v for k,v in enumerate(list(army))}}
    
    #Declare variables for game loop
    bullet_count = 1
    bullets={}
    no_victor = True
    
    #Start game loop
    while no_victor:

        #CODE FOR BULLETS
        bullets_hit = []
        targets_hit = []

        #Check if any current bullets hit
        for bullet, data in bullets.items():
            bullets[bullet]['dist'] += bullets[bullet]['speed']
            if bullets[bullet]['dist'] >= DIST:
                bullets_hit.append(bullet)
                targets_hit.append(bullets[bullet]['target'])
        
        #Remove bullets that hit
        for bullet in bullets_hit:
            bullets.pop(bullet)  
            
        #Fire off new bullets
        armies_to_be_removed = []
        for army in queues:
            #find first key
            fk = list(queues[army]['army'].keys())[0]
            if army in targets_hit:
                #Remove first soldier if hit
                queues[army]['army'].pop(fk)
                #Check if army has remaining soldiers
                if len(queues[army]['army']) == 0:
                    armies_to_be_removed.append(army)
            else:
                bullets[bullet_count]={'dist':0,'speed':queues[army]['army'][fk],'target':queues[army]['target']}
                bullet_count += 1
                #Rotate first soldier to the back
                x = queues[army]['army'][fk] 
                queues[army]['army'].pop(fk)
                queues[army]['army'][fk]=x
                
        #Remove current bullets if elimination occurs.        
        if len(armies_to_be_removed) > 0:
            bullets={}
              
        #Updates active_armies list
        for army in armies_to_be_removed:
            active_armies.remove(army)
            queues.pop(army)
            
        #Assign new targets
        for army in queues:
            if queues[army]['target'] not in active_armies:
                new_target=active_armies.index(army)+1
                if new_target > len(active_armies)-1:
                    new_target=0
                queues[army]['target']=active_armies[new_target]
           
        #Ends loops if one or zero armies remain
        if len(queues) <= 1:
                no_victor=False
    
    #return based on victor (or lack thereof)
    if active_armies == []:
        return (-1,())
    else:
        winning_army = active_armies[0]
        leftover_soldiers = list(queues[army]['army'].keys())
        
        return(winning_army,tuple(leftover_soldiers))
