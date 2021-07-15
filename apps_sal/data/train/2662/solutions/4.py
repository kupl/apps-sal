def shoot(a):
    main = {}
    for i, j in a:
        hit = 2 if j else 1
        main["p1"] = main.get("p1", 0) + i['P1'].count("X")*hit
        main["p2"] = main.get("p2", 0) + i['P2'].count("X")*hit
    return ["Draw!", ["Pete Wins!", "Phil Wins!"][main["p1"] < main["p2"]]][main["p1"] != main["p2"]]
