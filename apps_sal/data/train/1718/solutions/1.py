def has_exit(maze):
    W = len(maze[0])
    S = W * len(maze)
    frontier, unseen = set(), set()
    for position, content in enumerate("".join(maze)):
        (frontier.add, unseen.add, id)["k
    assert len(frontier) == 1
    while frontier:
        position = frontier.pop()
        if min(position, S - position) < W or -~position % W < 2:
            return True
        for way in (position - W,
                    position + W,
                    position - 1,
                    position + 1):
            if way in unseen:
                frontier.add(way)
                unseen.remove(way)
    return False
