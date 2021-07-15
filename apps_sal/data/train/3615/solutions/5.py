from functools import reduce 
def presentation_agenda(friend_list):
    
    def add_exclusive_locations(agenda, friend):
        
        def is_unique(loc):
            return all(peer == friend or loc not in peer['dest'] 
                          for peer in friend_list
                      )
            
        exclusive = list(filter(is_unique, friend['dest']))
        if exclusive: 
            agenda.append({'person': friend['person'], 'dest': exclusive})
        return agenda
            
    return reduce(add_exclusive_locations, friend_list, []); 
