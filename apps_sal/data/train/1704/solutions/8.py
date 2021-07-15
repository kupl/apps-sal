class PokerHand(object):

    def __init__(self, hand):
        self.hand = hand
        pass
    
    def handProcess(self, handList):
        suit = handList[0][1]
        isHandFlush = True
        
        seenCards = []
        seenPairs = []
        seenTriple = []
        seenFour = []
        
        for card in handList:
            # Detect flush hand
            if suit not in card:
                isHandFlush = False
            
            # Replace cards denomination by real value
            if card[0] == "T":
                handList[handList.index(card)], card = 10, 10
            elif card[0] == "J":
                handList[handList.index(card)], card = 11, 11
            elif card[0] == "Q":
                handList[handList.index(card)], card = 12, 12
            elif card[0] == "K":
                handList[handList.index(card)], card = 13, 13
            elif card[0] == "A":
                handList[handList.index(card)], card = 14, 14
            else:
                 handList[handList.index(card)], card = int(card[0]), int(card[0])
            
            # Check pairs, triple and four of a kind
            if card in seenCards:
                if card in seenTriple:
                    seenFour.append(card)
                    del seenTriple[seenTriple.index(card)]
                elif card in seenPairs:
                    seenTriple.append(card)
                    del seenPairs[seenPairs.index(card)]
                else:
                    seenPairs.append(card)
            seenCards.append(card)
            
            
        # Check if hand is straight
        handList = sorted(handList)
        if sum(handList) == (handList[-1]*(handList[-1]+1))/2-((handList[0]-1)*(handList[0])/2):
            isHandStraight = True
        else:
            isHandStraight = False
                
        # Store highest card
        highestCard = handList[-1]
        
        # Store highest hand value
        highestValue = 0
        
        # Store highest value after a match
        cardsOutsideCombination = []
        
        # Calculate hand score
        handScore = 0
        if highestCard == 14 and isHandStraight and isHandFlush:
            handScore = 9 # Royal Flush
        elif isHandStraight and isHandFlush:
            handScore = 8 # Straight Flush
            highestValue = highestCard
        elif len(seenFour) == 1:
            handScore = 7 # Four of a kind
            highestValue = seenFour[0]
            for card in handList:
                if card not in seenFour:
                    cardsOutsideCombination.append(card)
        elif len(seenTriple) == 1 and len(seenPairs) == 1:
            handScore = 6 # Full House
            highestValue = seenTriple[0]
        elif isHandFlush:
            handScore = 5 # Flush
        elif isHandStraight:
            handScore = 4 # Straight
        elif len(seenTriple) == 1:
            handScore = 3 # Three of a kind
            highestValue = seenTriple[0]
            for card in handList:
                if card not in seenTriple:
                    cardsOutsideCombination.append(card)
        elif len(seenPairs) == 2:
            handScore = 2 # Two pairs
            highestValue = sorted(seenPairs)[-1]
            for card in handList:
                if card not in seenPairs:
                    cardsOutsideCombination.append(card)
        elif len(seenPairs) == 1:
            handScore = 1 # Pair
            highestValue = seenPairs[0]
            for card in handList:
                if card not in seenPairs:
                    cardsOutsideCombination.append(card)
        
        
        return (handScore, highestValue, highestCard, cardsOutsideCombination, handList)
        
        
    def compare_with(self, other):
        hand1 = self.handProcess(self.hand.split())
        hand2 = self.handProcess(other.hand.split())
        
        # Check winner by hand combination score
        # Then by the value of the card of the combination
        # Then by the highest card of the hand
        # Then, iteratively, by the value of the highest card outside the combination
        # Then, iteratively, by the highest card of the hand when not entirely equal
        # Else, it's a tie !
        if hand1[0] > hand2[0]:
            return "Win"
        elif hand1[0] < hand2[0]:
            return "Loss"
        elif hand1[1] > hand2[1]:
            return "Win"
        elif hand1[1] < hand2[1]:
            return "Loss"
        else:
            if hand1[2] > hand2[2]:
                return "Win"
            elif hand1[2] < hand2[2]:
                return "Loss"
            for card in range(0, len(hand1[3])):
                if hand1[3][card] > hand2[3][card]:
                    return "Win"
                elif hand1[3][card] < hand2[3][card]:
                    return "Loss"
            for card in range(len(hand1[4])-1, -1, -1):
                if hand1[4][card] > hand2[4][card]:
                    return "Win"
                elif hand1[4][card] < hand2[4][card]:
                    return "Loss"
            return "Tie"
