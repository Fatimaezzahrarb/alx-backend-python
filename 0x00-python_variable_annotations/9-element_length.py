#!/usr/bin/env python3
'''Task 9.
'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Compute length of a list of the sequences.
    '''
    return [(i, len(i)) for i in lst]
