from dataclasses import dataclass

BLANK: str = ' '
START: str = BLANK * 9


@dataclass(frozen=True)
class Node:
    state: str = START
    turn: int = 0

    @property
    def is_goal(self) -> bool:
        if self.turn < 5:  # noqa: PLR2004
            return False

        target = 'ooo' if self.turn % 2 else 'xxx'

        return any(
            self.state[i] + self.state[j] + self.state[k] == target
            for i, j, k in [
                [0, 1, 2],
                [3, 4, 5],
                [6, 7, 8],
                [0, 3, 6],
                [1, 4, 7],
                [2, 5, 8],
                [0, 4, 8],
                [2, 4, 6],
            ]
        )

    @property
    def children(self) -> set:
        if self.turn == 0:
            return {
                Node('x' + BLANK * 8, 1),
                Node(BLANK + 'x' + BLANK * 7, 1),
                Node(BLANK * 4 + 'x' + BLANK * 4, 1),
            }

        return {
            Node(
                self.state[:i] + 'xo'[self.turn % 2] + self.state[i + 1 :],
                self.turn + 1,
            )
            for i in range(9)
            if self.state[i] == BLANK
        }
