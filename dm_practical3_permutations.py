"""
============================================================
PRACTICAL 3 — PERMUTATIONS
Discrete Mathematics | Python Implementation
============================================================
Features:
  - Generate all permutations of a given set of digits
  - Without repetition (standard permutations)
  - With repetition (n^r arrangements)
  - Display count and all arrangements

Sample Input/Output:
  Digits : [1, 2, 3]  |  r = 2

  WITHOUT Repetition (P(3,2) = 6):
    (1,2) (1,3) (2,1) (2,3) (3,1) (3,2)

  WITH Repetition (3^2 = 9):
    (1,1) (1,2) (1,3) (2,1) (2,2) (2,3) (3,1) (3,2) (3,3)
============================================================
"""

from itertools import permutations, product
from math import factorial


# ── Core functions ────────────────────────────────────────────

def perm_without_repetition(elements, r):
    """
    Generate all r-permutations WITHOUT repetition.
    Formula: P(n,r) = n! / (n-r)!
    Uses itertools.permutations under the hood.
    """
    n = len(elements)
    if r > n:
        print(f"  ⚠ r={r} > n={n}. Cannot generate without repetition.")
        return []
    result = list(permutations(elements, r))
    return result


def perm_with_repetition(elements, r):
    """
    Generate all r-permutations WITH repetition.
    Formula: n^r
    Uses itertools.product (Cartesian product).
    """
    result = list(product(elements, repeat=r))
    return result


def count_without_rep(n, r):
    """P(n,r) = n! / (n-r)!"""
    if r > n:
        return 0
    return factorial(n) // factorial(n - r)


def count_with_rep(n, r):
    """n^r"""
    return n ** r


def display_perms(label, perms, formula_count):
    """Pretty-print permutations with a label."""
    print(f"\n  {label} (Formula: {formula_count}, Generated: {len(perms)}):")
    if not perms:
        print("  (none)")
        return
    # Print in rows of 8
    for i, p in enumerate(perms):
        print("  " + str(p), end="")
        if (i + 1) % 8 == 0:
            print()
    print()  # newline at end


# ── Manual permutation generator (without itertools) ──────────
def _generate_perms_manual(elements, r, current, used, result):
    """Recursive backtracking — without repetition."""
    if len(current) == r:
        result.append(tuple(current))
        return
    for i, e in enumerate(elements):
        if not used[i]:
            used[i] = True
            current.append(e)
            _generate_perms_manual(elements, r, current, used, result)
            current.pop()
            used[i] = False


def perms_manual_no_rep(elements, r):
    """Manual implementation using backtracking."""
    result = []
    used = [False] * len(elements)
    _generate_perms_manual(elements, r, [], used, result)
    return result


def _generate_perms_rep_manual(elements, r, current, result):
    """Recursive — WITH repetition."""
    if len(current) == r:
        result.append(tuple(current))
        return
    for e in elements:
        current.append(e)
        _generate_perms_rep_manual(elements, r, current, result)
        current.pop()


def perms_manual_with_rep(elements, r):
    """Manual implementation — with repetition."""
    result = []
    _generate_perms_rep_manual(elements, r, [], result)
    return result


# ── Menu-driven interface ──────────────────────────────────────
def menu():
    print("\n" + "═" * 55)
    print("       DISCRETE MATHEMATICS — PERMUTATIONS")
    print("═" * 55)

    while True:
        print("""
┌─────────────────────────────────────────┐
│           PERMUTATIONS MENU             │
├─────────────────────────────────────────┤
│  1. Permutations without repetition     │
│  2. Permutations with repetition        │
│  3. Both (compare side by side)         │
│  4. Manual backtracking demo            │
│  0. Exit                                │
└─────────────────────────────────────────┘""")
        choice = input("  Enter choice: ").strip()
        if choice == "0":
            print("  Exiting PERMUTATION module.")
            break

        if choice not in ("1", "2", "3", "4"):
            print("  ❌ Invalid choice.")
            continue

        # Get input
        raw = input("\n  Enter digits/elements (space-separated): ").split()
        elements = []
        for x in raw:
            try:
                elements.append(int(x))
            except ValueError:
                elements.append(x)

        n = len(elements)
        r = int(input(f"  Enter r (arrange r items from {n}): "))

        if choice == "1":
            perms = perm_without_repetition(elements, r)
            fc = count_without_rep(n, r)
            display_perms(f"P({n},{r}) without repetition", perms, fc)

        elif choice == "2":
            perms = perm_with_repetition(elements, r)
            fc = count_with_rep(n, r)
            display_perms(f"P({n},{r}) with repetition", perms, fc)

        elif choice == "3":
            p1 = perm_without_repetition(elements, r)
            p2 = perm_with_repetition(elements, r)
            display_perms(f"WITHOUT repetition P({n},{r})", p1, count_without_rep(n, r))
            display_perms(f"WITH repetition {n}^{r}", p2, count_with_rep(n, r))

        elif choice == "4":
            print("\n  ── Manual Backtracking (no itertools) ──")
            p1 = perms_manual_no_rep(elements, r)
            display_perms(f"Manual WITHOUT rep P({n},{r})", p1, count_without_rep(n, r))
            p2 = perms_manual_with_rep(elements, r)
            display_perms(f"Manual WITH rep {n}^{r}", p2, count_with_rep(n, r))


if __name__ == "__main__":
    menu()
