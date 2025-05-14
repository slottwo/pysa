from ai.node import Node


def BrFS(node: Node):
    """
    Breadth-First Search

    - Time: O(b**d)
    - Space: O(b**d)

    A
    ├─ B
    │  ├─ D*
    │  └─ E
    └─ C
       ├─ F
       └─ G

    - Visit: A -> B -> C -> D
    - Space: A, B, C -> D, E -> F, G
    """

    queue = []

    while True:
        if node.is_goal:
            return node
        else:
            queue.extend(node.children)

        if not queue:
            return None

        node = queue.pop(0)
