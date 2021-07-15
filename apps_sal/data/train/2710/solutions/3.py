def scrabble_score(st): 

# Define point list as array
    onePt = ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]
    twoPt = ["D", "G"]
    threePt = ["B", "C", "M", "P"]
    fourPt = ["F", "H", "V", "W", "Y"]
    fivePt = ["K"]
    eightPt = ["J", "X"]
    tenPt = ["Q", "Z"]

# set pt as 0
    pt = 0

    if len(st) == 0 or st is None:          #if array is - or null then return 0
        return 0
    else:
        #reformat input string
        nSt = st.strip()
        nSt = nSt.upper()
        
        #check for every character against point lists 
        for char in nSt:
            if char in onePt:
                pt += 1
                continue
            elif char in twoPt:
                pt += 2
                continue
            elif char in threePt:
                pt += 3
                continue
            elif char in fourPt:
                pt += 4
                continue
            elif char in fivePt:
                pt += 5
                continue
            elif char in eightPt:
                pt += 8
                continue
            elif char in tenPt:
                pt += 10
                continue
    
    #return calculated pt
    return pt

