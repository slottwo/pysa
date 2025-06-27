from ai.node import Node


def BrFS(node: Node):
    queue = []

    while True:
        if node.is_goal:
            return node
        else:
            queue.extend(node.children)

        if not queue:
            return None

        node = queue.pop(0)
