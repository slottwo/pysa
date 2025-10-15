from pysa.node import Node, dataclass


@dataclass
class Node(Node):
    cost: int = 0
    parent: Node | None = None


def UCS(node):
    node.cost = 0
    frontier = [node]  # Min Heap
    explored = set()  # Hash

    while True:
        if not frontier:
            return None

        node = frontier.pop(0)
        if node.is_goal:
            return node
        explored.add(node)

        for child in node.children:
            if child not in explored:
                child.parent = node
                child.cost = node.cost + 1
                frontier.insert(child)
