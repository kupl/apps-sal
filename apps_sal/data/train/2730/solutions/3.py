def tickets(people):
    cashRegister = {25: 0, 50: 0, 100: 0};
    ticketPrice = 25;
    for paid in people:
        cashRegister[paid] += 1;
        while paid > ticketPrice:
            changeGiven = False;
            """ Check if we have a bill in the register that we use as change """
            for bill in sorted(cashRegister.keys(), reverse=True):
                """ Hand out hhange if possible and still needed """
                if (paid - ticketPrice >= bill) and (cashRegister[bill] > 0):
                    paid = paid - bill;
                    cashRegister[bill] -= 1;
                    changeGiven = True;
            """ Return "NO" if we were unable to give the change required """
            if (paid > ticketPrice) and (changeGiven == False):
                    return "NO";
    return "YES";
