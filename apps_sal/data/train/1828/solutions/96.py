from collections import Counter


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        if barcodes is None or len(barcodes) == 0:
            return []
        if len(barcodes) == 1:
            return barcodes

        counter = Counter(barcodes)
        num_occurrences = sorted(counter, key=lambda x: counter.get(x), reverse=True)
        elements = dict()

        for elem in num_occurrences:
            elements[elem] = counter[elem]

        output = [None] * len(barcodes)
        item_index = 0
        index = 0
        value = num_occurrences[0]
        value_index = 0
        for i in range(len(barcodes)):
            while output[index] is not None or output[index - 1] == value:
                index += 1
                index %= len(barcodes)
            output[index] = value
            item_index += 1
            index += 1
            index %= len(barcodes)
            if elements[value] == 1:
                value_index += 1
                if value_index >= len(num_occurrences):
                    return output
                value = num_occurrences[value_index]
            else:
                elements[value] -= 1

        return output
