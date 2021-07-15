how_many_bees=lambda h:h and sum(map('|'.join(map(''.join,h+list(zip(*h)))).count,('bee','eeb')))or 0
