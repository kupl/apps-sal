def shoot(results):
    pete = phil = 0

    for shots, double in results:
        pete += shots["P1"].count("X") * (1 + double)
        phil += shots["P2"].count("X") * (1 + double)

    return "Pete Wins!" if pete > phil else "Phil Wins!" if phil > pete else "Draw!"
