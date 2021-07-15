def player_manager(plrs):
    if not plrs: return []
    output = []
    contact, player = plrs.split(', ')[1::2], plrs.split(', ')[::2]
    
    for x in range(len(contact)):
        output.append({'player': player[x], 'contact': int(contact[x])})
        
    return output
