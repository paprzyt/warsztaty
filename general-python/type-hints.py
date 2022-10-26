from typing import List, Union, Optional

def sum_list(mylist: List[int]) -> int:
    return sum(mylist)

# Type alias
number = Union[int, float]

def sum_vals(x: number, y: number) -> number:
    return x + y
