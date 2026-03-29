"""
============================================================
PRACTICAL 6 — COMPLETE GRAPH CHECKER
Discrete Mathematics | Python Implementation
============================================================
Features:
  - Represent undirected graph using adjacency matrix
  - Determine if graph is COMPLETE (Kn)
  - A graph is complete iff every pair of distinct
    vertices has exactly one edge connecting them
  - Additional info: edges, degree sequence

Sample Input/Output:
  n = 4 vertices (K4 check)
  Adjacency matrix (K4):
    0 1 1 1
    1 0 1 1
    1 1 0 1
    1 1 1 0
  Expected edges : 6  (n*(n-1)/2)
  Actual edges   : 6
  Is Complete    : True  ✓

  Incomplete graph:
    0 1 0
    1 0 1
    0 1 0
  Missing edge   : (1,3)
  Is Complete    : False ✗
============================================================
"""


class Graph:
    def __init__(self, n, matrix=None):
        """
        n      : number of vertices (labeled 1..n)
        matrix : n×n adjacency matrix (0/1), optional
        """
        self.n = n
        self.vertices = list(range(1, n + 1))
        if matrix:
            self._validate_matrix(matrix)
            self.matrix = matrix
        else:
            self.matrix = [[0] * n for _ in range(n)]

    def _validate_matrix(self, matrix):
        """Basic checks on matrix format."""
        assert len(matrix) == self.n, "Row count must equal n"
        for row in matrix:
            assert len(row) == self.n, "Column count must equal n"
        for i in range(self.n):
            assert matrix[i][i] == 0, f"Self-loop at vertex {i+1} not allowed"

    # ── Add edge ──────────────────────────────────────────────
    def add_edge(self, u, v):
        """Add undirected edge between vertices u and v (1-indexed)."""
        self.matrix[u - 1][v - 1] = 1
        self.matrix[v - 1][u - 1] = 1   # undirected

    # ── Display matrix ────────────────────────────────────────
    def display_matrix(self):
        print("\n  Adjacency Matrix:")
        print("    " + "  ".join(str(v) for v in self.vertices))
        for i, row in enumerate(self.matrix):
            print(f"  {self.vertices[i]} │ " + "  ".join(str(x) for x in row))

    # ── Degree of each vertex ─────────────────────────────────
    def degree(self, v):
        """Return degree of vertex v (1-indexed)."""
        return sum(self.matrix[v - 1])

    def degree_sequence(self):
        """Return sorted list of all vertex degrees."""
        return sorted([self.degree(v) for v in self.vertices], reverse=True)

    # ── Count edges ───────────────────────────────────────────
    def edge_count(self):
        """Count total edges (each counted once for undirected)."""
        return sum(self.matrix[i][j]
                   for i in range(self.n)
                   for j in range(i + 1, self.n))

    # ── Complete graph check ──────────────────────────────────
    def is_complete(self):
        """
        A graph Kn is complete iff:
          Every pair (i,j) with i≠j has matrix[i][j] = 1
        Expected edges = n*(n-1)//2
        """
        missing = []
        for i in range(self.n):
            for j in range(self.n):
                if i != j and self.matrix[i][j] != 1:
                    missing.append((i + 1, j + 1))
        return len(missing) == 0, missing

    # ── Expected edge count for Kn ────────────────────────────
    def expected_edges_complete(self):
        return self.n * (self.n - 1) // 2

    # ── Full report ───────────────────────────────────────────
    def report(self):
        self.display_matrix()
        complete, missing = self.is_complete()
        actual = self.edge_count()
        expected = self.expected_edges_complete()

        print(f"\n  Graph Statistics:")
        print(f"    Vertices       : {self.n}")
        print(f"    Actual edges   : {actual}")
        print(f"    Expected (Kn)  : {expected}")
        print(f"    Degree sequence: {self.degree_sequence()}")

        if complete:
            print(f"\n  ✓ This is a COMPLETE graph K{self.n}")
        else:
            # Show only first few missing edges
            sample = missing[:5]
            print(f"\n  ✗ NOT a complete graph.")
            print(f"    Missing {len(missing)//2} edge(s), e.g.: "
                  + ", ".join(f"({u},{v})" for u, v in sample[:3]))

    # ── Generate Kn ───────────────────────────────────────────
    @classmethod
    def complete(cls, n):
        """Return the complete graph Kn."""
        g = cls(n)
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                g.add_edge(i, j)
        return g


# ── Input helper ──────────────────────────────────────────────
def input_graph():
    n = int(input("\n  Number of vertices (n): "))
    print(f"  Vertices: {{1, 2, ..., {n}}}")
    print("  Enter edges as 'u v' (one per line). Type 'done' to finish.")
    g = Graph(n)
    while True:
        raw = input("  Edge: ").strip()
        if raw.lower() == "done":
            break
        try:
            u, v = map(int, raw.split())
            if 1 <= u <= n and 1 <= v <= n and u != v:
                g.add_edge(u, v)
            else:
                print(f"  ⚠ Vertices must be in 1..{n} and u ≠ v.")
        except ValueError:
            print("  ⚠ Enter two integers.")
    return g


def input_matrix():
    n = int(input("\n  Number of vertices (n): "))
    print(f"  Enter {n}×{n} adjacency matrix row by row:")
    matrix = []
    for i in range(n):
        row = list(map(int, input(f"  Row {i+1}: ").split()))
        if len(row) != n:
            print(f"  ⚠ Expected {n} values per row.")
            return None
        matrix.append(row)
    try:
        return Graph(n, matrix)
    except AssertionError as e:
        print(f"  ⚠ Invalid matrix: {e}")
        return None


# ── Menu ──────────────────────────────────────────────────────
def menu():
    print("\n" + "═" * 55)
    print("   DISCRETE MATHEMATICS — COMPLETE GRAPH CHECKER")
    print("═" * 55)

    while True:
        print("""
┌─────────────────────────────────────────┐
│         COMPLETE GRAPH CHECKER MENU     │
├─────────────────────────────────────────┤
│  1. Input graph via edges               │
│  2. Input graph via adjacency matrix    │
│  3. Generate Kn (complete graph)        │
│  4. Run built-in demos                  │
│  0. Exit                                │
└─────────────────────────────────────────┘""")
        choice = input("  Enter choice: ").strip()

        if choice == "0":
            print("  Exiting COMPLETE GRAPH module.")
            break

        elif choice == "1":
            g = input_graph()
            g.report()

        elif choice == "2":
            g = input_matrix()
            if g:
                g.report()

        elif choice == "3":
            n = int(input("  Generate K_n for n = "))
            g = Graph.complete(n)
            g.report()

        elif choice == "4":
            print("\n  ── DEMO 1: K4 (Complete) ──")
            g1 = Graph.complete(4)
            g1.report()

            print("\n\n  ── DEMO 2: Path graph P3 (Not Complete) ──")
            g2 = Graph(3, [[0,1,0],[1,0,1],[0,1,0]])
            g2.report()

            print("\n\n  ── DEMO 3: K5 (Complete) ──")
            g3 = Graph.complete(5)
            g3.report()

        else:
            print("  ❌ Invalid choice.")


if __name__ == "__main__":
    menu()
