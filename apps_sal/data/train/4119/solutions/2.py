def sort_emotions(arr, reverse, ordered_emotions={smiley: idx for idx, smiley in enumerate('T_T :( :| :) :D'.split())}):
    return sorted(arr, reverse=reverse, key=ordered_emotions.get)
