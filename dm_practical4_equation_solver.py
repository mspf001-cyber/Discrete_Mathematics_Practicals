"""
============================================================
PRACTICAL 4 — EQUATION SOLVER
Discrete Mathematics | Python Implementation
============================================================
Problem:
  Find all non-negative integer solutions to:
    x1 + x2 + ... + xn = C
  where C ≤ 10 (brute-force approach)

Method:
  - Brute force: nested iteration using itertools.product
  - Filter all n-tuples (x1..xn) where sum == C
  - Each xi ∈ {0, 1, ..., C}

Sample Input/Output:
  n = 3, C = 4
  Solutions found: 15
  (0, 0, 4) (0, 1, 3) (0, 2, 2) (0, 3, 1) (0, 4, 0)
  (1, 0, 3) (1, 1, 2) (1, 2, 1) (1, 3, 0) (2, 0, 2) ...

  Theoretical count (stars & bars): C(C+n-1, n-1) = C(6,2) = 15 ✓
============================================================
"""

from itertools import product
from math import comb


# ── Core solver ───────────────────────────────────────────────

def solve_equation(n, C):
    """
    Brute-force: generate all n-tuples from {0..C}^n
    and keep those whose sum equals C.
    Time complexity: O(C^n)  — acceptable for C ≤ 10, n ≤ 5
    """
    solutions = []
    # Each variable ranges 0..C; product gives all combinations
    for combo in product(range(C + 1), repeat=n):
        if sum(combo) == C:
            solutions.append(combo)
    return solutions


def theoretical_count(n, C):
    """
    Stars & Bars formula:
    Number of non-negative integer solutions to x1+...+xn = C
    = C(C + n - 1, n - 1)
    """
    return comb(C + n - 1, n - 1)


def display_solutions(solutions, n, C):
    """Print solutions in a neat table."""
    var_names = [f"x{i+1}" for i in range(n)]
    header = "  " + "  ".join(f"{v:>4}" for v in var_names) + "  │  Sum"
    print(f"\n  {header}")
    print("  " + "─" * (len(header) - 2))
    for sol in solutions:
        row = "  ".join(f"{x:>4}" for x in sol)
        print(f"  {row}  │  {sum(sol)}")
    print(f"\n  Total solutions found   : {len(solutions)}")
    print(f"  Theoretical (Stars&Bars): {theoretical_count(n, C)}")
    match = "✓ Match" if len(solutions) == theoretical_count(n, C) else "✗ Mismatch"
    print(f"  Verification            : {match}")


def equation_label(n):
    """Return a string like 'x1 + x2 + x3'."""
    return " + ".join(f"x{i+1}" for i in range(n))


# ── Demo: show solution structure visually ────────────────────
def stars_and_bars_visual(C, n=2):
    """
    Visual aid for n=2: show how C stars split into 2 bins.
    (Only practical for small C)
    """
    if n != 2 or C > 8:
        return
    print(f"\n  Stars-and-bars visual for {equation_label(n)} = {C}:")
    for x1 in range(C + 1):
        x2 = C - x1
        bar = "★" * x1 + "│" + "★" * x2
        print(f"    x1={x1}, x2={x2}  →  [{bar}]")


# ── Menu ──────────────────────────────────────────────────────
def menu():
    print("\n" + "═" * 55)
    print("    DISCRETE MATHEMATICS — EQUATION SOLVER")
    print("═" * 55)
    print("  Solves: x1 + x2 + ... + xn = C")
    print("  Constraint: C ≤ 10 (brute-force feasible)")

    while True:
        print("""
┌─────────────────────────────────────────┐
│           EQUATION SOLVER MENU          │
├─────────────────────────────────────────┤
│  1. Solve custom equation               │
│  2. Run demo (n=2, C=4)                 │
│  3. Run demo (n=3, C=4)                 │
│  4. Enumerate all cases for fixed C     │
│  0. Exit                                │
└─────────────────────────────────────────┘""")
        choice = input("  Enter choice: ").strip()

        if choice == "0":
            print("  Exiting EQUATION SOLVER module.")
            break

        elif choice == "1":
            try:
                n = int(input("  Number of variables (n): "))
                C = int(input("  Target sum (C ≤ 10): "))
                if C > 10 or C < 0:
                    print("  ⚠ C must be between 0 and 10.")
                    continue
                if n < 1:
                    print("  ⚠ n must be ≥ 1.")
                    continue
                if n > 6:
                    print("  ⚠ n > 6 may be slow. Proceeding anyway...")
                print(f"\n  Solving: {equation_label(n)} = {C}")
                solutions = solve_equation(n, C)
                display_solutions(solutions, n, C)
                stars_and_bars_visual(C, n)
            except ValueError:
                print("  ⚠ Enter valid integers.")

        elif choice == "2":
            n, C = 2, 4
            print(f"\n  DEMO — {equation_label(n)} = {C}")
            solutions = solve_equation(n, C)
            display_solutions(solutions, n, C)
            stars_and_bars_visual(C, n)

        elif choice == "3":
            n, C = 3, 4
            print(f"\n  DEMO — {equation_label(n)} = {C}")
            solutions = solve_equation(n, C)
            display_solutions(solutions, n, C)

        elif choice == "4":
            try:
                C = int(input("  Fix C (≤ 10): "))
                if not (0 <= C <= 10):
                    print("  ⚠ Must be 0–10.")
                    continue
                print(f"\n  Counts for fixed C={C}:")
                print(f"  {'n':>4}  {'Solutions':>12}  {'Stars&Bars':>12}")
                print("  " + "─" * 34)
                for n in range(1, 7):
                    sols = len(solve_equation(n, C))
                    theory = theoretical_count(n, C)
                    print(f"  {n:>4}  {sols:>12}  {theory:>12}")
            except ValueError:
                print("  ⚠ Enter a valid integer.")

        else:
            print("  ❌ Invalid choice.")


if __name__ == "__main__":
    menu()
