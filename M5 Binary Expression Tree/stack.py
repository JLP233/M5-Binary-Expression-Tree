class Stack:
    "Simple LIFO stack used by BinaryExpressionTree (self-contained)."
    def __init__(self):
        self._data = []

    def push(self, x):
        self._data.append(x)

    def pop(self):
        if not self._data:
            raise IndexError("Pop From Empty Stack")
        return self._data.pop()

    def top(self):
        if not self._data:
            raise IndexError("Top From Empty Stack")
        return self._data[-1]

    def is_empty(self):
        return not self._data

    def __len__(self):
        return len(self._data)
