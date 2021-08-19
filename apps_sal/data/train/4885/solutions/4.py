def find_gatecrashers(people, invitations):
    guests = []
    for (guest, otherGuests) in invitations:
        guests.append(guest)
        guests.extend(otherGuests)
    return sorted(set(people).difference(set(guests)))
