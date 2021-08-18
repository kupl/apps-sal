def men_still_standing(cards):

    print(cards)

    Team_A = 11
    Team_B = 11

    Yellows = []
    Reds = []

    for event in cards:

        if Team_A == 6 or Team_B == 6:
            return (Team_A, Team_B)

        else:

            print(event)

            if event[-1] == "R" and event[0:(len(event) - 1)] not in Reds:

                print("Red card event")

                Reds.append(event[0:(len(event) - 1)])
                print("Red Cards", Reds)

                if event[0] == "A":
                    Team_A -= 1
                    print("Team A remaining = ", str(Team_A))
                else:
                    Team_B -= 1
                    print("Team B remaining = ", str(Team_B))

            elif event[-1] == "Y" and event[0:(len(event) - 1)] in Yellows and event[0:(len(event) - 1)] not in Reds:
                print("2nd Yellow Card event, Player sent off", Reds)
                Reds.append(event[0:(len(event) - 1)])

                if event[0] == "A":
                    Team_A -= 1
                    print("Team A remaining = ", str(Team_A))
                else:
                    Team_B -= 1
                    print("Team B remaining = ", str(Team_B))

            elif event[-1] == "Y":

                if event[0:(len(event) - 1)] in Reds:
                    print("Player already sent off")
                else:
                    Yellows.append(event[0:(len(event) - 1)])
                    print("Yellow card issued to", Yellows)
            else:
                print("player already sent off!")

    print(Team_A, Team_B)

    return(Team_A, Team_B)
