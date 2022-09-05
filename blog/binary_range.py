from __future__ import annotations
import math
from dataclasses import dataclass
from typing import Union

# We don't include complex numbers
# in our Numeric data type for simiplicity's
# sake
Numeric = Union[int, float]

@dataclass
class ValueRange:
    minvalue: Numeric
    maxvalue: Numeric
        
    left : ValueRange = None
    right : ValueRange = None
        
    def __iter__(self):
        yield self
        if self.left is not None:
            for elem in self.left:
                yield elem
        if self.right is not None:
            for elem in self.right:
                yield elem
                
    def _range(self):
        return self.maxvalue - self.minvalue
    
    def __eq__(self, other):
        return self._range() == other._range()
    
    def __lt__(self, other):
        return self._range() < other._range()
    
    def __le__(self, other):
        return self._range() <= other._range()
    
    def __gt__(self, other):
        return self._range() > other._range()
    
    def __ge__(self, other):
        return self._range() >= other._range()

def build_tree(val_range, floor_range):
    minval, maxval = val_range.minvalue, val_range.maxvalue
    
    floors = ((maxval - minval) // 2) / floor_range
    if floors < 1:
        return val_range
    
    midval = minval + math.floor(floors)*floor_range
    val_range.left = build_tree(ValueRange(minval, midval), floor_range)
    val_range.right = build_tree(ValueRange(midval, maxval), floor_range)
    
    return val_range