from typing import Iterable


def flatten(list_of_lists: Iterable):
    return [item for sublist in list_of_lists for item in sublist]
