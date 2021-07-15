def bob(what):
    db = {}
    db["werewolf"] = "Silver knife or bullet to the heart"
    db["vampire"] = "Behead it with a machete"
    db["wendigo"] = "Burn it to death"
    db["shapeshifter"] = "Silver knife or bullet to the heart"
    db["angel"] = "Use the angelic blade"
    db["demon"] = "Use Ruby's knife, or some Jesus-juice"
    db["ghost"] = "Salt and iron, and don't forget to burn the corpse"
    db["dragon"] = "You have to find the excalibur for that"
    db["djinn"] = "Stab it with silver knife dipped in a lamb's blood"
    db["pagan god"] = "It depends on which one it is"
    db["leviathan"] = "Use some Borax, then kill Dick"
    db["ghoul"] = "Behead it"
    db["jefferson starship"] = "Behead it with a silver blade"
    db["reaper"] = "If it's nasty, you should gank who controls it"
    db["rugaru"] = "Burn it alive"
    db["skinwalker"] = "A silver bullet will do it"
    db["phoenix"] = "Use the colt"
    db["witch"] = "They are humans"
    if what in db:
      return db[what]+", idjits!"
    else:
      return "I have friggin no idea yet"+", idjits!"
