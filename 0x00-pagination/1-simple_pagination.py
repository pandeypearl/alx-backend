#!/usr/bin/env python3
""" Simple Pagination """

from typing import Tuple, List
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns tuple containing start_index and end_index
    corresponding to the range of indexes to return
    in a list for those particlar pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


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
        """ Finds correct indexes to paginate dataset """
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0
        csv_size = len(self.dataset())
        start, end - index_range(page, page_size)
        end = min(end, csv_size)
        if start >= csv_size:
            return []
        return self.dataset()[start:end]
