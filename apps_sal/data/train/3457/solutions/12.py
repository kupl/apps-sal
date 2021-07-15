from functools import reduce
from operator import and_, or_
from typing import NamedTuple, Tuple, Callable, Any

Exam = Projects = int
Activities = Tuple[Exam, Projects]

class Rule(NamedTuple):
    limits: Activities
    relation: Callable[[bool, bool], bool]
    result: Any

RULES = (
    Rule((90, 10), or_, 100),
    Rule((75, 4), and_, 90),
    Rule((50, 1), and_, 75),
)

def final_grade(*scores: Activities) -> int:
    for rule in RULES:
        pairs = tuple(zip(scores, rule.limits))
        if pairs and reduce(rule.relation, (score > limit for score, limit in pairs)):
            return rule.result
    return 0
