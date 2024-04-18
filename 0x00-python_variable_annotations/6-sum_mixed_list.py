#!/usr/bin/env python3
'''Task 6.
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Computes sum of a list of integers and the floating point numbers.
    '''
    return float(sum(mxd_lst))
