from ai.node import Node


def DFS(node: Node):
    stack = [node]

    while stack:
        node = stack.pop()

        if node.is_goal:
            return node
        else:
            stack.extend(node.children)


def DLS(node: Node, depth: int):
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
    depth = 0

    while True:
        found, remaining = DLS(node, depth)
        if not found:
            return found
        if not remaining:
            return None
        depth += 1
