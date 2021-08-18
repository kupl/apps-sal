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
            if suit not in card:
                isHandFlush = False

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

        handList = sorted(handList)
        if sum(handList) == (handList[-1] * (handList[-1] + 1)) / 2 - ((handList[0] - 1) * (handList[0]) / 2):
            isHandStraight = True
        else:
            isHandStraight = False

        highestCard = handList[-1]

        highestValue = 0

        cardsOutsideCombination = []

        handScore = 0
        if highestCard == 14 and isHandStraight and isHandFlush:
            handScore = 9
        elif isHandStraight and isHandFlush:
            handScore = 8
            highestValue = highestCard
        elif len(seenFour) == 1:
            handScore = 7
            highestValue = seenFour[0]
            for card in handList:
                if card not in seenFour:
                    cardsOutsideCombination.append(card)
        elif len(seenTriple) == 1 and len(seenPairs) == 1:
            handScore = 6
            highestValue = seenTriple[0]
        elif isHandFlush:
            handScore = 5
        elif isHandStraight:
            handScore = 4
        elif len(seenTriple) == 1:
            handScore = 3
            highestValue = seenTriple[0]
            for card in handList:
                if card not in seenTriple:
                    cardsOutsideCombination.append(card)
        elif len(seenPairs) == 2:
            handScore = 2
            highestValue = sorted(seenPairs)[-1]
            for card in handList:
                if card not in seenPairs:
                    cardsOutsideCombination.append(card)
        elif len(seenPairs) == 1:
            handScore = 1
            highestValue = seenPairs[0]
            for card in handList:
                if card not in seenPairs:
                    cardsOutsideCombination.append(card)

        return (handScore, highestValue, highestCard, cardsOutsideCombination, handList)

    def compare_with(self, other):
        hand1 = self.handProcess(self.hand.split())
        hand2 = self.handProcess(other.hand.split())

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
            for card in range(len(hand1[4]) - 1, -1, -1):
                if hand1[4][card] > hand2[4][card]:
                    return "Win"
                elif hand1[4][card] < hand2[4][card]:
                    return "Loss"
            return "Tie"
