from __future__ import annotations
import heapq
from dataclasses import dataclass
from typing import Optional, Tuple

@dataclass(order=True)
class _PriorityItem:
    # Invert severity (max-heap behavior via min-heap): higher severity -> smaller key
    key: Tuple[int,int]
    name: str
    severity: int

class TriageSystem:
    "Priority queue places higher severity conditions first and ties use FIFO arrival order."
    _arrival_counter = 0  # class-level

    def __init__(self) -> None:
        self._pq = []  # private heap

   