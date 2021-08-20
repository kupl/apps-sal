def bubble(l):
    (bubbling, bubbles) = (True, [])
    while bubbling:
        bubbling = False
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                (l[i], l[i + 1]) = (l[i + 1], l[i])
                bubbling = True
                bubbles.append(l[:])
    return bubbles
