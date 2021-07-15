def souls(character, build):
    
    DICT={'pyromancer':(1,[10, 12, 11, 12, 9, 12, 10, 8]),
          'warrior':(4,[11, 8, 12, 13, 13, 11, 9, 9]),
          'knight':(5,[14, 10, 10, 11, 11, 10, 9, 11]),
          'wanderer':(3,[10, 11, 10, 10, 14, 12, 11, 8]),
          'thief':(5,[9, 11, 9, 9, 15, 10, 12, 11]),
          'bandit':(4,[12, 8, 14, 14, 9, 11, 8, 10]),
          'hunter':(4,[11, 9, 11, 12, 14, 11, 9, 9]),
          'sorcerer':(3,[8, 15, 8, 9, 11, 8, 15, 8]),
          'cleric':(2,[11, 11, 9, 12, 8, 11, 8, 14]),
          'deprived':(6,[11, 11, 11, 11, 11, 11, 11, 11])
          }
    
    
    list_upgrade_souls=[673, 690, 707, 724, 741, 758, 775, 793, 811,829]
    levels_after_11 = [round(pow(x+12, 3) * 0.02 + pow(x+12, 2) * 3.06 + 105.6 * (x+12) - 895) for x in range(5000)]
    list_upgrade_souls.extend(levels_after_11)
    cnt_souls=0
    
    actual_powers=DICT[character][1]
    actual_level=DICT[character][0]
    desired_level=sum([x1 - x2 for (x1, x2) in zip(build, actual_powers)]) + actual_level
    for i in range(actual_level-1,desired_level-1):
        cnt_souls+=list_upgrade_souls[i]

    return 'Starting as a {}, level {} will require {} souls.'.format(character,desired_level,cnt_souls)
    

