#!/usr/bin/env python3
'''
Implement a Class that Processes csv dataset
'''
import csv
import math
from typing import List
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        ''' Returns a page of results given the number and size '''
        self.dataset()
        assert (isinstance(page, int) and isinstance(page_size, int))
        assert page > 0 and page_size > 0

        idxs = index_range(page, page_size)

        if idxs[0] > len(self.__dataset) or idxs[1] > len(self.__dataset):
            return []

        return self.__dataset[idxs[0]:idxs[1]]
