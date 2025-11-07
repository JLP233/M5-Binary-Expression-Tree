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

def sample_tree_for_traversals() -> Node:
    n8 = Node("8")
    n3 = Node("3"); n10 = Node("10")
    n1 = Node("1"); n6 = Node("6"); n14 = Node("14")
    n4 = Node("4"); n7 = Node("7"); n13 = Node("13")
    n8.left, n8.right = n3, n10
    n3.left, n3.right = n1, n6
    n6.left, n6.right = n4, n7
    n10.right = n14
    n14.left = n13
    return n8

def run_demo():
    root = sample_tree_for_traversals()
    pre, ino, post = [], [], []
    preorder(root, pre); inorder(root, ino); postorder(root, post)
    print("Preorder:", " ".join(pre))
    print("Inorder:", " ".join(ino))
    print("Postorder:", " ".join(post))
    print()

    pre_seq = "Q W E R T Y U I".split()
    in_seq  = "E W T R Q Y U I".split()
    r1 = build_from_pre_in(pre_seq, in_seq)
    pre1, ino1, post1 = [], [], []
    preorder(r1, pre1); inorder(r1, ino1); postorder(r1, post1)
    print("Reconstructed (Pre+In) Traversals:")
    print("Preorder:", " ".join(pre1))
    print("Inorder:", " ".join(ino1))
    print("Postorder:", " ".join(post1))
    print()

    post_seq = "J I L M N K H".split()
    in2_seq  = "J I H L K M N".split()
    r2 = build_from_post_in(post_seq, in2_seq)
    pre2, ino2, post2 = [], [], []
    preorder(r2, pre2); inorder(r2, ino2); postorder(r2, post2)
    print("Reconstructed (Post+In) Traversals:")
    print("Preorder:", " ".join(pre2))
    print("Inorder:", " ".join(ino2))
    print("Postorder:", " ".join(post2))

if __name__ == "__main__":
    run_demo()
