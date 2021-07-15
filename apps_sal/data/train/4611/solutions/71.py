def animals(head,legs):
    restlegs = legs - 2*head
    chicken = head - restlegs / 2
    cow = head - chicken
    if cow.is_integer() and cow >= 0:
        if chicken.is_integer() and chicken >= 0:
            return (int(chicken), int(cow))
        else:
            return "No solutions"
    elif head == 0 and legs == 0:
        return [0, 0]
    else:
        return "No solutions"
