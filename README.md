# Search Algorithms

## Breadth-First Search

- Time: $O(b^d)$
- Space: $O(b^d)$

### Sample

    A
    ├─ B
    │  ├─ D*
    │  └─ E
    └─ C
        ├─ F
        └─ G


- Visit: A -> B -> C -> D
- Space: A, B, C -> D, E -> F, G

## Depth-First Search

- Time: $O(b^m)$
- Space: $O(b \cdot m)$

# Sample:

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

| Visit | Space |
| - | - |
| A | A, + B, C |
| B | A, B, C + D, E |
| D | A, B, C, D, E + H, I |
| H | A, B, C, D, E, I |
| I | A, B, C, E, I |
| E | A, B, C, E + J, K |
| J | A, B, C, E, J, K |
| K | A, B, C, E, K |
| C | A, C + F, G |
| F | A, C, F, G + L, M |
| L | A, C, F, G, L, M |
| M | A, C, F, G, M |

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


## Depth Limited Search

- Time: $O(b^l)$
- Space: $O(b \cdot l)$


## Iterative Deepening Depth-First Search

- Time: $O(b^m)$
- Space: $O(b \cdot m)$