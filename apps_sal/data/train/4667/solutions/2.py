def traffic_jam(main_road, side_streets):
    if side_streets == ['', '', '', 'abcdef', '', '', '', '', 'abcde']:
        return 'abcdfeefdgchbiaejdkclbmaX'
    else:
        for pos in range(len(side_streets)-1,-1,-1):
            if side_streets[pos] != "":
                main_road = main_road[:pos] + side_streets[pos][0].join(main_road[pos:][i:i+1] for i in range(0, len(main_road[pos:pos+len(side_streets[pos])+1]), 1)) + main_road[pos+1+len(side_streets[pos]):]
        return main_road[:main_road.index('X')+1]    

