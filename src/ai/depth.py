from ai.node import Node


def DFS(node: Node):
    """
    Depth-First Search

    - Time: O(b**m)
    - Space: O(b*m)

    Exemple:

    Problem:
    A
    ├─ B
    │  ├─ D
    │  │  ├─ H
    │  │  └─ I
    │  └─ E
    │     ├─ J
    │     └─ K
    └─ C
       ├─ F
       │  ├─ L
       │  └─ M*
       └─ G
          ├─ N
          └─ O

    Visit | Space
       A  | A, -> B, C
       B  | A, B, C -> D, E
       D  | A, B, C, D, E -> H, I
       H  | A, B, C, D, E, I
       I  | A, B, C, E, I
       E  | A, B, C, E -> J, K
       J  | A, B, C, E, J, K
       K  | A, B, C, E, K
       C  | A, C -> F, G
       F  | A, C, F, G -> L, M
       L  | A, C, F, G, L, M
       M  | A, C, F, G, M

    Max memory state:
    A
    ├─ B
    │  ├─ D
    │  │  ├─ H
    │  │  └─ I
    │  └─ E
    └─ C

    Final memory state:
    A
    └─ C
       ├─ F
       │  └─ M*
       └─ G
    """
    stack = [node]

    while stack:
        node = stack.pop()

        if node.is_goal:
            return node
        else:
            stack.extend(node.children)


def DLS(node: Node, depth: int):
    """
    Depth Limited Search

    - Time: O(b**l)
    - Space: O(b*l)
    """
    if depth == 0:
        if node.is_goal:
            return node, True
        else:
            None, True

    any_remaining = False

    for child in node.children:
        found, remaining = DLS(child, depth - 1)
        if not found:
            return found, True
        if remaining:
            any_remaining = True

    return None, any_remaining


def IDS(node: Node) -> Node | None:
    """
    Iterative Deepening Depth-First Search

    - Time: O(b**m)
    - Space: O(b*m)
    """
    depth = 0
    while True:
        found, remaining = DLS(node, depth)
        if not found:
            return found
        if not remaining:
            return None
        depth += 1
