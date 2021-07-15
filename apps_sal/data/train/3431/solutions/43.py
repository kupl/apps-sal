def warn_the_sheep(queue):
    
    for i in range(len(queue)):
        if queue[-1] == 'wolf':
            return 'Pls go away and stop eating my sheep'
        elif queue[i] =='wolf':
            return f'Oi! Sheep number {len(queue)-1-i}! You are about to be eaten by a wolf!'

