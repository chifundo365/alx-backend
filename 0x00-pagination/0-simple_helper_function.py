#!/usr/bin/env python3
'''
Implement a function that calculates the indexes given the range
'''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    '''
    Calculates the start index and the end index corresponding
    to the range of indexes to return in a list for those
    particular pagination parameters.
    '''
    return ((page * page_size) - page_size, (page * page_size))
