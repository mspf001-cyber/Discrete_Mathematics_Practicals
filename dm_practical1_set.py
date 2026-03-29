"""
============================================================
PRACTICAL 1 — SET CLASS
Discrete Mathematics | Python Implementation
============================================================
Operations:
  - is_member, powerset, subset
  - union, intersection, complement
  - difference, symmetric difference
  - cartesian product
  - Menu-driven interface

Sample Input/Output:
  Universal Set : {1, 2, 3, 4, 5}
  Set A         : {1, 2, 3}
  Set B         : {3, 4, 5}
  Union         : {1, 2, 3, 4, 5}
  Intersection  : {3}
  Complement A  : {4, 5}
============================================================
"""


class Set:
    def __init__(self, elements=None):
        """Initialize set from a list (duplicates removed)."""
        self.elements = list(dict.fromkeys(elements)) if elements else []

    # ── Core helpers ─────────────────────────────────────────
    def __repr__(self):
        return "{" + ", ".join(str(e) for e in self.elements) + "}" if self.elements else "∅"

    def __len__(self):
        return len(self.elements)

    def __eq__(self, other):
        return sorted(self.elements) == sorted(other.elements)

    # ── 1. Membership ─────────────────────────────────────────
    def is_member(self, x):
        """Return True if x belongs to this set."""
        return x in self.elements

    # ── 2. Power Set ──────────────────────────────────────────
    def powerset(self):
        """Return the power set as a list of Set objects."""
        n = len(self.elements)
        result = []
        for mask in range(1 << n):          # iterate over 2^n bitmasks
            subset = [self.elements[i] for i in range(n) if mask & (1 << i)]
            result.append(Set(subset))
        return result

    # ── 3. Subset check ───────────────────────────────────────
    def is_subset(self, other):
        """Return True if self ⊆ other."""
        return all(x in other.elements for x in self.elements)

    # ── 4. Union ──────────────────────────────────────────────
    def union(self, other):
        """Return A ∪ B."""
        combined = self.elements + [x for x in other.elements if x not in self.elements]
        return Set(combined)

    # ── 5. Intersection ───────────────────────────────────────
    def intersection(self, other):
        """Return A ∩ B."""
        return Set([x for x in self.elements if x in other.elements])

    # ── 6. Complement ─────────────────────────────────────────
    def complement(self, universal):
        """Return A' with respect to the universal set."""
        return Set([x for x in universal.elements if x not in self.elements])

    # ── 7. Difference ─────────────────────────────────────────
    def difference(self, other):
        """Return A − B (elements in A but not in B)."""
        return Set([x for x in self.elements if x not in other.elements])

    # ── 8. Symmetric Difference ───────────────────────────────
    def symmetric_difference(self, other):
        """Return A △ B = (A − B) ∪ (B − A)."""
        return self.difference(other).union(other.difference(self))

    # ── 9. Cartesian Product ──────────────────────────────────
    def cartesian_product(self, other):
        """Return A × B as a list of tuples."""
        return [(a, b) for a in self.elements for b in other.elements]


# ── Utility: parse user input ─────────────────────────────────
def parse_set(prompt):
    raw = input(prompt + " (space-separated values): ").split()
    # Try converting to int, fall back to str
    elements = []
    for r in raw:
        try:
            elements.append(int(r))
        except ValueError:
            elements.append(r)
    return Set(elements)


# ── Menu-driven interface ──────────────────────────────────────
def menu():
    print("\n" + "═" * 55)
    print("        DISCRETE MATHEMATICS — SET OPERATIONS")
    print("═" * 55)

    universal = parse_set("Enter Universal Set U")
    A = parse_set("Enter Set A")
    B = parse_set("Enter Set B")

    while True:
        print("""
┌─────────────────────────────────────────┐
│           SET OPERATIONS MENU           │
├─────────────────────────────────────────┤
│  1. Membership check                    │
│  2. Power Set of A                      │
│  3. Is A a subset of B?                 │
│  4. Union (A ∪ B)                       │
│  5. Intersection (A ∩ B)                │
│  6. Complement of A (A')               │
│  7. Difference (A − B)                  │
│  8. Symmetric Difference (A △ B)        │
│  9. Cartesian Product (A × B)           │
│  10. Display current sets               │
│  0. Exit                                │
└─────────────────────────────────────────┘""")

        choice = input("  Enter choice: ").strip()

        if choice == "1":
            try:
                x = int(input("  Element to check: "))
            except ValueError:
                x = input("  Element to check: ")
            print(f"  {x} ∈ A? → {A.is_member(x)}")
            print(f"  {x} ∈ B? → {B.is_member(x)}")

        elif choice == "2":
            ps = A.powerset()
            print(f"  Power Set of A (2^{len(A)} = {len(ps)} subsets):")
            for i, s in enumerate(ps):
                print(f"    {i}: {s}")

        elif choice == "3":
            print(f"  A ⊆ B? → {A.is_subset(B)}")
            print(f"  B ⊆ A? → {B.is_subset(A)}")

        elif choice == "4":
            print(f"  A ∪ B = {A.union(B)}")

        elif choice == "5":
            print(f"  A ∩ B = {A.intersection(B)}")

        elif choice == "6":
            print(f"  A' (w.r.t U) = {A.complement(universal)}")
            print(f"  B' (w.r.t U) = {B.complement(universal)}")

        elif choice == "7":
            print(f"  A − B = {A.difference(B)}")
            print(f"  B − A = {B.difference(A)}")

        elif choice == "8":
            print(f"  A △ B = {A.symmetric_difference(B)}")

        elif choice == "9":
            cp = A.cartesian_product(B)
            print(f"  A × B ({len(cp)} pairs) = {{", end=" ")
            print(", ".join(str(p) for p in cp), end=" }\n")

        elif choice == "10":
            print(f"  U = {universal}")
            print(f"  A = {A}")
            print(f"  B = {B}")

        elif choice == "0":
            print("  Exiting SET module. Goodbye!")
            break
        else:
            print("  ❌ Invalid choice. Try again.")


if __name__ == "__main__":
    menu()
