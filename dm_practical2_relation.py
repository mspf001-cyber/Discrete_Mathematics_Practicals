"""
============================================================
PRACTICAL 2 — RELATION CLASS
Discrete Mathematics | Python Implementation
============================================================
Features:
  - Represent relation using adjacency matrix
  - Check: Reflexive, Symmetric, Anti-symmetric, Transitive
  - Identify: Equivalence Relation, Partial Order

Sample Input/Output:
  n = 3, Set = {1, 2, 3}
  Pairs: (1,1) (2,2) (3,3) (1,2) (2,1)
  Matrix:
    1 1 0
    1 1 0
    0 0 1
  Reflexive     : True
  Symmetric     : True
  Anti-symmetric: False
  Transitive    : True
  Equivalence   : True
  Partial Order : False
============================================================
"""


class Relation:
    def __init__(self, n, pairs):
        """
        n     : number of elements in the set {1, 2, ..., n}
        pairs : list of tuples (a, b) representing the relation
        """
        self.n = n
        self.elements = list(range(1, n + 1))
        # Build n×n adjacency matrix (0-indexed internally)
        self.matrix = [[0] * n for _ in range(n)]
        for (a, b) in pairs:
            self.matrix[a - 1][b - 1] = 1

    # ── Display ───────────────────────────────────────────────
    def display_matrix(self):
        print("\n  Relation Matrix (rows/cols = elements):")
        print("    " + "  ".join(str(e) for e in self.elements))
        for i, row in enumerate(self.matrix):
            print(f"  {self.elements[i]} │ " + "  ".join(str(v) for v in row))

    def get_pairs(self):
        """Return the relation as a list of (a,b) pairs."""
        return [
            (self.elements[i], self.elements[j])
            for i in range(self.n)
            for j in range(self.n)
            if self.matrix[i][j] == 1
        ]

    # ── 1. Reflexive: (a,a) ∈ R for all a ───────────────────
    def is_reflexive(self):
        return all(self.matrix[i][i] == 1 for i in range(self.n))

    # ── 2. Symmetric: (a,b) ∈ R → (b,a) ∈ R ────────────────
    def is_symmetric(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.matrix[i][j] == 1 and self.matrix[j][i] != 1:
                    return False
        return True

    # ── 3. Anti-symmetric: (a,b)∈R ∧ (b,a)∈R → a=b ─────────
    def is_antisymmetric(self):
        for i in range(self.n):
            for j in range(self.n):
                if i != j and self.matrix[i][j] == 1 and self.matrix[j][i] == 1:
                    return False
        return True

    # ── 4. Transitive: (a,b)∈R ∧ (b,c)∈R → (a,c)∈R ────────
    def is_transitive(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.matrix[i][j] == 1:          # (i+1, j+1) ∈ R
                    for k in range(self.n):
                        if self.matrix[j][k] == 1:  # (j+1, k+1) ∈ R
                            if self.matrix[i][k] != 1:
                                return False
        return True

    # ── 5. Equivalence = Reflexive + Symmetric + Transitive ──
    def is_equivalence(self):
        return self.is_reflexive() and self.is_symmetric() and self.is_transitive()

    # ── 6. Partial Order = Reflexive + Anti-sym + Transitive ─
    def is_partial_order(self):
        return self.is_reflexive() and self.is_antisymmetric() and self.is_transitive()

    # ── Full Report ───────────────────────────────────────────
    def report(self):
        self.display_matrix()
        print(f"\n  Pairs in R : {self.get_pairs()}")
        print("\n  ── Property Check ──────────────────────")
        print(f"  Reflexive      : {self.is_reflexive()}")
        print(f"  Symmetric      : {self.is_symmetric()}")
        print(f"  Anti-symmetric : {self.is_antisymmetric()}")
        print(f"  Transitive     : {self.is_transitive()}")
        print("\n  ── Relation Type ───────────────────────")
        print(f"  Equivalence Relation : {self.is_equivalence()}")
        print(f"  Partial Order        : {self.is_partial_order()}")


# ── Input helper ──────────────────────────────────────────────
def get_relation_input():
    print("\n" + "═" * 55)
    print("       DISCRETE MATHEMATICS — RELATION CLASS")
    print("═" * 55)

    n = int(input("\n  Enter number of elements in set (n): "))
    print(f"  Set = {{1, 2, ..., {n}}}")

    print("  Enter pairs as 'a b' one per line.")
    print("  Type 'done' when finished.")

    pairs = []
    while True:
        raw = input("  Pair: ").strip()
        if raw.lower() == "done":
            break
        try:
            a, b = map(int, raw.split())
            if 1 <= a <= n and 1 <= b <= n:
                pairs.append((a, b))
            else:
                print(f"  ⚠ Values must be between 1 and {n}.")
        except ValueError:
            print("  ⚠ Enter two integers separated by space.")

    return Relation(n, pairs)


# ── Predefined examples for quick demo ────────────────────────
def demo_relations():
    print("\n  ── DEMO: Equivalence Relation on {{1,2,3}} ──")
    r1 = Relation(3, [(1,1),(2,2),(3,3),(1,2),(2,1)])
    r1.report()

    print("\n\n  ── DEMO: Partial Order (≤) on {{1,2,3}} ──")
    r2 = Relation(3, [(1,1),(2,2),(3,3),(1,2),(1,3),(2,3)])
    r2.report()

    print("\n\n  ── DEMO: Neither (random) on {{1,2,3}} ──")
    r3 = Relation(3, [(1,2),(2,3)])
    r3.report()


def menu():
    while True:
        print("""
┌─────────────────────────────────────────┐
│         RELATION CLASS MENU             │
├─────────────────────────────────────────┤
│  1. Input custom relation               │
│  2. Run built-in demos                  │
│  0. Exit                                │
└─────────────────────────────────────────┘""")
        choice = input("  Enter choice: ").strip()
        if choice == "1":
            rel = get_relation_input()
            rel.report()
        elif choice == "2":
            demo_relations()
        elif choice == "0":
            print("  Exiting RELATION module.")
            break
        else:
            print("  ❌ Invalid choice.")


if __name__ == "__main__":
    menu()
