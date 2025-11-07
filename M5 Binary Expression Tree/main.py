from M5_Binary_Expression_Tree import BinaryExpressionTree

EXAMPLES = [
    "5 3 +",
    "8 2 - 3 +",
    "5 3 8 * +",
    "6 2 / 3 +",
    "5 8 + 3 -",
    "5 3 + 8 *",
    "8 2 3 * + 6 -",
    "5 3 8 * + 2 /",
    "8 2 + 3 6 * -",
    "5 3 + 8 2 / -",
]

def run_demo():
    print("Binary Expression Tree \n")
    for pf in EXAMPLES:
        T = BinaryExpressionTree()
        T.build_from_postfix(pf)
        print(f"Infix Expression:   {T.infix_traversal()}")
        print(f"Postfix Expression: {T.postfix_traversal()}")
        print(f"Evaluated Result:   {T.evaluate_tree()}\n")

if __name__ == "__main__":
    run_demo()
