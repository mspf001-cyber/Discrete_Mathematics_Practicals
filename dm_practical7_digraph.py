"""
============================================================
PRACTICAL 7 — DIRECTED GRAPH DEGREE
Discrete Mathematics | Python Implementation
============================================================
Features:
  - Represent directed graph using adjacency matrix
  - Compute in-degree and out-degree for each vertex
  - Display degree table
  - Verify Handshaking Lemma:
      Σ in-degree = Σ out-degree = |E|
  - Identify source (in=0) and sink (out=0) vertices

Sample Input/Output:
  n=4, Directed edges: (1→2)(1→3)(2→4)(3→4)(4→1)
  Adjacency Matrix:
       1  2  3  4
    1│ 0  1  1  0
    2│ 0  0  0  1
    3│ 0  0  0  1
    4│ 1  0  0  0

  Vertex │ In-deg │ Out-deg │ Total
  ───────┼────────┼─────────┼──────
       1 │      1 │       2 │     3
       2 │      1 │       1 │     2
       3 │      1 │       1 │     2
       4 │      2 │       1 │     3

  Total edges   : 5
  Σ In-degree   : 5 ✓
  Σ Out-degree  : 5 ✓
  Sources (in=0): none
  Sinks (out=0) : none
============================================================
"""


class DiGraph:
    def __init__(self, n, matrix=None):
        """
        n      : number of vertices (labeled 1..n)
        matrix : n×n adjacency matrix (0/1, directed)
                 matrix[i][j]=1 means edge i→j
        """
        self.n = n
        self.vertices = list(range(1, n + 1))
        if matrix:
            self.matrix = matrix
        else:
            self.matrix = [[0] * n for _ in range(n)]

    # ── Add directed edge ─────────────────────────────────────
    def add_edge(self, u, v):
        """Add directed edge u → v (1-indexed)."""
        if u == v:
            print(f"  ⚠ Self-loops ignored ({u}→{v})")
            return
        self.matrix[u - 1][v - 1] = 1

    # ── Display matrix ────────────────────────────────────────
    def display_matrix(self):
        print("\n  Adjacency Matrix (row i → col j means i→j):")
        print("    " + "  ".join(str(v) for v in self.vertices))
        for i, row in enumerate(self.matrix):
            print(f"  {self.vertices[i]} │ " + "  ".join(str(x) for x in row))

    # ── In-degree of vertex v ─────────────────────────────────
    def in_degree(self, v):
        """In-degree = number of edges ENTERING v = sum of column (v-1)."""
        col = v - 1
        return sum(self.matrix[row][col] for row in range(self.n))

    # ── Out-degree of vertex v ────────────────────────────────
    def out_degree(self, v):
        """Out-degree = number of edges LEAVING v = sum of row (v-1)."""
        return sum(self.matrix[v - 1])

    # ── Edge count ────────────────────────────────────────────
    def edge_count(self):
        """Total number of directed edges."""
        return sum(self.matrix[i][j]
                   for i in range(self.n)
                   for j in range(self.n))

    # ── Sources and Sinks ─────────────────────────────────────
    def sources(self):
        """Vertices with in-degree = 0."""
        return [v for v in self.vertices if self.in_degree(v) == 0]

    def sinks(self):
        """Vertices with out-degree = 0."""
        return [v for v in self.vertices if self.out_degree(v) == 0]

    def isolated(self):
        """Vertices with both in-degree and out-degree = 0."""
        return [v for v in self.vertices
                if self.in_degree(v) == 0 and self.out_degree(v) == 0]

    # ── Degree table ──────────────────────────────────────────
    def degree_table(self):
        print("\n  ┌────────┬─────────┬──────────┬─────────┐")
        print("  │ Vertex │ In-deg  │ Out-deg  │  Total  │")
        print("  ├────────┼─────────┼──────────┼─────────┤")
        total_in = 0
        total_out = 0
        for v in self.vertices:
            ind = self.in_degree(v)
            outd = self.out_degree(v)
            total = ind + outd
            total_in += ind
            total_out += outd
            print(f"  │  {v:>4}  │  {ind:>5}  │   {outd:>5}  │  {total:>5}  │")
        print("  ├────────┼─────────┼──────────┼─────────┤")
        print(f"  │  SUM   │  {total_in:>5}  │   {total_out:>5}  │         │")
        print("  └────────┴─────────┴──────────┴─────────┘")
        return total_in, total_out

    # ── Handshaking lemma verification ────────────────────────
    def verify_handshaking(self):
        """
        Directed Handshaking Lemma:
          Σ in-degree = Σ out-degree = |E|
        """
        E = self.edge_count()
        total_in = sum(self.in_degree(v) for v in self.vertices)
        total_out = sum(self.out_degree(v) for v in self.vertices)
        ok_in = total_in == E
        ok_out = total_out == E
        print(f"\n  Handshaking Lemma Verification:")
        print(f"    |E| (edges)     = {E}")
        print(f"    Σ in-degree    = {total_in}  {'✓' if ok_in else '✗'}")
        print(f"    Σ out-degree   = {total_out}  {'✓' if ok_out else '✗'}")

    # ── Special vertex analysis ────────────────────────────────
    def special_vertices(self):
        src = self.sources()
        snk = self.sinks()
        iso = self.isolated()
        print(f"\n  Special Vertices:")
        print(f"    Sources  (in=0)     : {src if src else 'none'}")
        print(f"    Sinks    (out=0)    : {snk if snk else 'none'}")
        print(f"    Isolated (in=out=0) : {iso if iso else 'none'}")

    # ── Find all edges ────────────────────────────────────────
    def get_edges(self):
        return [(self.vertices[i], self.vertices[j])
                for i in range(self.n)
                for j in range(self.n)
                if self.matrix[i][j] == 1]

    # ── Full report ───────────────────────────────────────────
    def report(self):
        self.display_matrix()
        edges = self.get_edges()
        print(f"\n  Directed Edges ({len(edges)}): "
              + ", ".join(f"{u}→{v}" for u, v in edges))
        self.degree_table()
        self.verify_handshaking()
        self.special_vertices()


# ── Input helpers ─────────────────────────────────────────────
def input_digraph_edges():
    n = int(input("\n  Number of vertices (n): "))
    print(f"  Vertices: {{1, 2, ..., {n}}}")
    print("  Enter directed edges as 'u v' (u→v). Type 'done' to finish.")
    g = DiGraph(n)
    while True:
        raw = input("  Edge u→v: ").strip()
        if raw.lower() == "done":
            break
        try:
            u, v = map(int, raw.split())
            if 1 <= u <= n and 1 <= v <= n:
                g.add_edge(u, v)
            else:
                print(f"  ⚠ Vertices must be in range 1..{n}")
        except ValueError:
            print("  ⚠ Enter two integers.")
    return g


def input_digraph_matrix():
    n = int(input("\n  Number of vertices (n): "))
    print(f"  Enter {n}×{n} adjacency matrix row by row:")
    matrix = []
    for i in range(n):
        row = list(map(int, input(f"  Row {i+1}: ").split()))
        if len(row) != n:
            print(f"  ⚠ Need exactly {n} values.")
            return None
        matrix.append(row)
    return DiGraph(n, matrix)


# ── Menu ──────────────────────────────────────────────────────
def menu():
    print("\n" + "═" * 55)
    print("   DISCRETE MATHEMATICS — DIRECTED GRAPH DEGREE")
    print("═" * 55)

    while True:
        print("""
┌─────────────────────────────────────────┐
│       DIRECTED GRAPH DEGREE MENU        │
├─────────────────────────────────────────┤
│  1. Input graph via directed edges      │
│  2. Input graph via adjacency matrix    │
│  3. Run built-in demos                  │
│  0. Exit                                │
└─────────────────────────────────────────┘""")
        choice = input("  Enter choice: ").strip()

        if choice == "0":
            print("  Exiting DIRECTED GRAPH module.")
            break

        elif choice == "1":
            g = input_digraph_edges()
            g.report()

        elif choice == "2":
            g = input_digraph_matrix()
            if g:
                g.report()

        elif choice == "3":
            print("\n  ── DEMO 1: 4-vertex cycle + extras ──")
            # Edges: 1→2, 1→3, 2→4, 3→4, 4→1
            g1 = DiGraph(4)
            for e in [(1,2),(1,3),(2,4),(3,4),(4,1)]:
                g1.add_edge(*e)
            g1.report()

            print("\n\n  ── DEMO 2: Graph with source and sink ──")
            # 1 is source, 4 is sink
            g2 = DiGraph(4)
            for e in [(1,2),(1,3),(2,4),(3,4)]:
                g2.add_edge(*e)
            g2.report()

            print("\n\n  ── DEMO 3: Tournament on K3 ──")
            # Complete directed: 1→2, 2→3, 1→3
            g3 = DiGraph(3)
            for e in [(1,2),(2,3),(1,3)]:
                g3.add_edge(*e)
            g3.report()

        else:
            print("  ❌ Invalid choice.")


if __name__ == "__main__":
    menu()
