from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, List, Dict

@dataclass
class Node:
    val: str
    left: Optional['Node']=None
    right: Optional['Node']=None

def preorder(n: Optional[Node], out: List[str]):
    if not n: return
    out.append(str(n.val))
    preorder(n.left, out)
    preorder(n.right, out)

def inorder(n: Optional[Node], out: List[str]):
    if not n: return
    inorder(n.left, out)
    out.append(str(n.val))
    inorder(n.right, out)

def postorder(n: Optional[Node], out: List[str]):
    if not n: return
    postorder(n.left, out)
    postorder(n.right, out)
    out.append(str(n.val))

def build_from_pre_in(pre: List[str], inorder_seq: List[str]) -> Optional[Node]:
    if not pre or not inorder_seq:
        return None
    index_map: Dict[str,int] = {v:i for i,v in enumerate(inorder_seq)}
    def helper(ps, pe, is_, ie) -> Optional[Node]:
        if ps>pe or is_>ie: return None
        root_val = pre[ps]
        idx = index_map[root_val]
        left_len = idx - is_
        root = Node(root_val)
        root.left = helper(ps+1, ps+left_len, is_, idx-1)
        root.right = helper(ps+left_len+1, pe, idx+1, ie)
        return root
    return helper(0, len(pre)-1, 0, len(inorder_seq)-1)

def build_from_post_in(post: List[str], inorder_seq: List[str]) -> Optional[Node]:
    if not post or not inorder_seq:
        return None
    index_map: Dict[str,int] = {v:i for i,v in enumerate(inorder_seq)}
    def helper(ps, pe, is_, ie) -> Optional[Node]:
        if ps>pe or is_>ie: return None
        root_val = post[pe]
        idx = index_map[root_val]
        left_len = idx - is_
        root = Node(root_val)
        root.left = helper(ps, ps+left_len-1, is_, idx-1)
        root.right = helper(ps+left_len, pe-1, idx+1, ie)
        return root
    return helper(0, len(post)-1, 0, len(inorder_seq)-1)

