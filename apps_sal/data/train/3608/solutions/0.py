database = "werewolf : Silver knife or bullet to the heart\nvampire : Behead it with a machete\nwendigo : Burn it to death\nshapeshifter : Silver knife or bullet to the heart\nangel : Use the angelic blade\ndemon : Use Ruby's knife, or some Jesus-juice\nghost : Salt and iron, and don't forget to burn the corpse\ndragon : You have to find the excalibur for that\ndjinn : Stab it with silver knife dipped in a lamb's blood\npagan god : It depends on which one it is\nleviathan : Use some Borax, then kill Dick\nghoul : Behead it\njefferson starship : Behead it with a silver blade\nreaper : If it's nasty, you should gank who controls it\nrugaru : Burn it alive\nskinwalker : A silver bullet will do it\nphoenix : Use the colt\nwitch : They are humans\nelse : I have friggin no idea yet"
answers = {line.split(' : ')[0]: line.split(' : ')[1] for line in database.splitlines()}


def bob(what):
    return answers.get(what, answers['else']) + ', idjits!'
