from re import findall; repeat_adjacent=lambda s: len(findall(r"((.)\2+(?!\2)){2,}",s))
