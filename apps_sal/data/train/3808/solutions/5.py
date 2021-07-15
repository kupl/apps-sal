def knight_or_knave(said):
    f,t="Knave! Do not trust.","Knight!"
    if isinstance(said,bool):return [f,t][said]
    elif isinstance(said,str):return [f,t][eval(said)]
