from functools import reduce 
def presentation_agenda(friend_list):
    def add_exclusive_locations(agenda, presenter):
        def is_unique(location):
            return False if any(location in friend['dest'] 
                for friend in filter(lambda f: f != presenter, friend_list)
            ) else True

        exclusive = list(filter(is_unique, presenter['dest']))
        if exclusive:
            agenda.append({'person': presenter['person'], 'dest': exclusive})
        return agenda
            
    return reduce(add_exclusive_locations, friend_list, []); 
