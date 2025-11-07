from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, List
from stack import Stack

OPERATORS = {"+", "-", "*", "/"}

@dataclass
class TreeNode:
    value: str
    left: Optional['TreeNode'] = None
    right: Optional['TreeNode'] = None

class BinaryExpressionTree:
    "ADT per spec: build from postfix; evaluate; infix & postfix traversals."
    def __init__(self) -> None:
        self.root: Optional[TreeNode] = None
