from __future__ import annotations
from typing import Iterator, Tuple, List, Iterable
from math import sqrt

class DataPoint:
    def __init__(self, initial: Iterable[float]) -> None:
        self._originals: Tuple[float, ...] = tuple(initial)
        self.dimensions: Tuple[float, ...] = tuple(initial)
    
    @property
    def num_dimensions(self):
        return len(self.dimensions)
    
    def distance(self, other: DataPoint) -> float:
        combined: Iterable[Tuple[float, float]] = zip(self.dimensions, other.dimensions)
        differences: List[float] = [(x - y) ** 2 for x, y in combined]  
        return sqrt(sum(differences))

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, DataPoint):
            return NotImplemented
        return self.dimensions == __o.dimensions

    def __repr__(self) -> str:
        return self._originals.__repr__()