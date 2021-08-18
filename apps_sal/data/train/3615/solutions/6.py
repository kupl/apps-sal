from functools import reduce


def presentation_agenda(friend_list):

    def add_exclusive_locations(agenda, friend):
        locations_visited_by_peers = reduce(
            lambda lst, p: lst + p['dest'] if p != friend else lst,
            friend_list,
            []
        )

        def is_unique(loc):
            return loc not in locations_visited_by_peers

        exclusive = list(filter(is_unique, friend['dest']))
        if exclusive:
            agenda.append({'person': friend['person'], 'dest': exclusive})
        return agenda

    return reduce(add_exclusive_locations, friend_list, [])
