import math
from abc import ABC
from abc import abstractmethod
from typing import Dict
from typing import List
from typing import Union

from tabulate import tabulate

from apps_sal.dataset import Dataset
from apps_sal.logger import get_logger


def pass_at_k(results: Dict[Union[int, str], List[float]],
              k: int = 1,
              n: Union[int, None] = None) -> float:  # pylint: disable=invalid-name
    correct = []
    for result in results.values():
        n = len(result) if n is None else n
        if n == 0:
            get_logger().warning('No submission evaluated. This problem is treated as wrong.')
            continue
        c = len([e for e in result if e >= 1.0])
        k = min(n, k)
        correct.append(1 - math.comb(n - c, k) / math.comb(n, k))
    score = sum(correct)
    total = len(results)
    return score / total


def strict_accuracy(results: Dict[Union[int, str], List[float]]) -> float:
    correct = []
    for result in results.values():
        if len(result) == 0:
            get_logger().warning('No submission evaluated. This problem is treated as wrong.')
            continue
        for score in result:
            if score >= 1.0:
                correct.append(1)
                break
        else:
            correct.append(0)
    correct = sum(correct)
    total = len(results)
    return correct / total


def testcase_accuracy(results: Dict[Union[int, str], List[float]]) -> float:
    correct = []
    for result in results.values():
        if len(result) == 0:
            get_logger().warning('No submission evaluated. This problem is treated as wrong.')
            continue
        correct.append(sum(result) / len(result))
    correct = sum(correct)
    total = len(results)
    return correct / total


class Metric(ABC):

    def __init__(self, title: str = 'Result') -> None:
        self.title: str = title

    def print_report(self, results: Dict[Union[int, str], List[float]],
                     dataset: Union[Dataset, None] = None, file=None):
        redirect = lambda *x: print(*x, file=file)

        # title
        redirect(self.title)

        # table entries
        entries = []

        if dataset is not None:
            # introductory
            introductories = dataset.filter(lambda elem: elem.metadata['difficulty'] == 'introductory')
            introductories = [int(elem.id) for elem in introductories]
            introductory_results = {id: result for id, result in results.items() if int(id) in introductories}
            introductory_accuracy = self(introductory_results) * 100 if len(introductory_results) > 0 else None
            entries.append(('introductory', len(introductory_results), introductory_accuracy))

            # interview
            interviews = dataset.filter(lambda elem: elem.metadata['difficulty'] == 'interview')
            interviews = [int(elem.id) for elem in interviews]
            interview_results = {id: result for id, result in results.items() if int(id) in interviews}
            interview_accuracy = self(interview_results) * 100 if len(interview_results) > 0 else None
            entries.append(('interview', len(interview_results), interview_accuracy))

            # competition
            competitions = dataset.filter(lambda elem: elem.metadata['difficulty'] == 'competition')
            competitions = [int(elem.id) for elem in competitions]
            competition_results = {id: result for id, result in results.items() if int(id) in competitions}
            competition_accuracy = self(competition_results) * 100 if len(competition_results) > 0 else None
            entries.append(('competition', len(competition_results), competition_accuracy))

        # total
        total_accuracy = self(results) * 100
        entries.append(('total', len(results), total_accuracy))

        # print table
        redirect(tabulate(entries, headers=['', 'counts', 'strict accuracy (%)'], floatfmt='.2f'))
        redirect()

    def __call__(self, results: Dict[Union[int, str], List[float]]) -> float:
        return self.evaluate(results)

    @abstractmethod
    def evaluate(self, results: Dict[Union[int, str], List[float]]) -> float:
        '''Evaluate the result.

        Args:
            results: A dictionary that contains the testcase-wise score for each problem.
        '''


class StrictAccuracy(Metric):

    def __init__(self, title: str = 'Strict Accuracy Report') -> None:
        super().__init__(title)

    def evaluate(self, results: Dict[Union[int, str], List[float]]) -> float:
        return strict_accuracy(results)


class TestcaseAccuracy(Metric):

    def __init__(self, title: str = 'Testcase Accuracy Report') -> None:
        super().__init__(title)

    def evaluate(self, results: Dict[Union[int, str], List[float]]) -> float:
        return testcase_accuracy(results)


class PassAtK(Metric):

    def __init__(self,
                 k: int = 1,
                 n: Union[int, None] = None,
                 title: Union[None, str] = None) -> None:
        super().__init__(f'Pass@{k} Report' if title is None else title)
        self.k: int = k
        self.n: Union[int, None] = n  # pylint: disable=invalid-name

    def evaluate(self, results: Dict[Union[int, str], List[float]]) -> float:
        return pass_at_k(results, self.k, self.n)
