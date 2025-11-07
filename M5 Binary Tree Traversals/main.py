from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, List, Dict

@dataclass
class Node:
    val: str
    left: Optional['Node']=None
    right: Optional['Node']=None