def animals(heads, legs):
    if (heads-((legs-(heads*2))/2))%1 != 0 or (heads-((legs-(heads*2))/2))%1 < 0 or int((legs-(heads*2))/2) < 0:
        return 'No solutions'
    elif heads==0 and legs==0:
        return 0,0
    elif heads <= 0 or legs <= 0:
        return "No solutions"
    else:
        hen = heads-int((legs-(heads*2))/2)
        cow = int((legs-(heads*2))/2)
        if hen <0 or cow < 0:
            return "No solutions"
        else:
            return hen,cow
