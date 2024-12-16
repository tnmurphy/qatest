import json
from collections import Counter

class Response:
    def __init__(self, data, status_code):
        self.data = data
        self.status_code = status_code

    def json(self):
        return self.data

    def text(self):
        return json.dumps(self.data)

def median(numbers):
    "Get the median of a list of numbers"
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    if length % 2 == 0:
        right = length // 2
        left = right - 1
        median = (sorted_numbers[left] + sorted_numbers[right]) / 2
    else:
        median = sorted_numbers[length // 2]

    response = Response({"median": median}, 200)
    return response


def mode(numbers):
    """ 
    find the mode which is the most common number in the list or 
    if there are multiple numbers that are equally common, return all of them
    But a mode cannot be the whole list - if all numbers are equally 
    common then there is no mode.
    e.g. 
    [ 1, 2, 3, 2, 2, 4 ]  -> [2]
    [ 3, 1, 4, 2, 2, 4 ]  -> [2, 4]
    """
    counter = Counter(numbers)
    most_common = counter.most_common() # ordered by most common

    mode = [most_common[0][0]]
    current_count = most_common[0][1]

    for number, count in most_common[1:]:
        if count == current_count:
            mode.append(number)
        else:
            break

    response = Response({"mode": mode}, 200)

    return response
