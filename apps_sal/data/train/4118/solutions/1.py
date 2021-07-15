def identify_weapon(character):
    #insert your code here...FOR CHIMA!
    try:
        return character + "-" + {
        "Laval":"Shado Valious", "Cragger":"Vengdualize",
        "Lagravis":"Blazeprowlor","Crominus":"Grandorius",
        "Tormak":"Tygafyre", "LiElla":"Roarburn"
        }[character]
    except:
        return "Not a character"
