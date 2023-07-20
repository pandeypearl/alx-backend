#!/usr/bin/env python3
""" Simple helper function index_range """

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns tuple containing start_index and end_index
    corresponding to the range of indexes to return
    in a list for those particlar pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
