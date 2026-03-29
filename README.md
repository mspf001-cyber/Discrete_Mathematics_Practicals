# Discrete Mathematics — Python Practicals
**B.E. Computer Science & Engineering**

> 7 fully executable Python programs covering core Discrete Mathematics topics.
> No third-party libraries required — standard Python 3 only.

---

## What is the Master Launcher?

`dm_master_launcher.py` is a **single entry-point program** that loads and runs all 7 practicals from one unified menu. Instead of remembering 7 filenames and opening each separately, you just run one file:

```bash
python dm_master_launcher.py
```

You'll see this:

```
══════════════════════════════════════════════════════
    DISCRETE MATHEMATICS — PRACTICAL LAB
    B.E. Computer Science & Engineering
══════════════════════════════════════════════════════

  Select a Practical:
  ┌──────────────────────────────────────────┐
  │  1. SET Class                            │
  │  2. RELATION Class                       │
  │  3. PERMUTATIONS                         │
  │  4. EQUATION SOLVER                      │
  │  5. POLYNOMIAL EVALUATION                │
  │  6. COMPLETE GRAPH CHECKER               │
  │  7. DIRECTED GRAPH DEGREE                │
  │  0. Exit                                 │
  └──────────────────────────────────────────┘
```

It uses Python's `importlib` to dynamically import the selected practical's `menu()` function and run it — returning to the master menu when you exit. Each practical still works independently too.

---

## File Structure

```
dm_master_launcher.py          ← Start here (runs all practicals)
dm_practical1_set.py           ← Practical 1: SET Class
dm_practical2_relation.py      ← Practical 2: RELATION Class
dm_practical3_permutations.py  ← Practical 3: Permutations
dm_practical4_equation_solver.py ← Practical 4: Equation Solver
dm_practical5_polynomial.py    ← Practical 5: Polynomial Evaluation
dm_practical6_complete_graph.py ← Practical 6: Complete Graph Checker
dm_practical7_digraph.py       ← Practical 7: Directed Graph Degree
README.md                      ← This file
```

> All 8 files must be in the **same folder** for the master launcher to work.

---

## Requirements

| Requirement | Detail |
|-------------|--------|
| Python | 3.6 or higher |
| Libraries | None (standard library only) |
| OS | Windows / Linux / macOS |

---

## How to Run

### Option A — Master Launcher (recommended)
```bash
python dm_master_launcher.py
```

### Option B — Run a single practical directly
```bash
python dm_practical1_set.py
python dm_practical2_relation.py
# ... and so on
```

---

## Practical-by-Practical Reference

---

### Practical 1 — SET Class
**File:** `dm_practical1_set.py`

Implements a `Set` class from scratch with the following operations:

| Method | Description |
|--------|-------------|
| `is_member(x)` | Check if x belongs to the set |
| `powerset()` | All subsets using bitmask technique (2ⁿ subsets) |
| `is_subset(other)` | Check A ⊆ B |
| `union(other)` | A ∪ B |
| `intersection(other)` | A ∩ B |
| `complement(universal)` | A' with respect to universal set U |
| `difference(other)` | A − B |
| `symmetric_difference(other)` | A △ B = (A−B) ∪ (B−A) |
| `cartesian_product(other)` | A × B (all ordered pairs) |

**Sample Interaction:**
```
U = {1, 2, 3, 4, 5}
A = {1, 2, 3}
B = {3, 4, 5}

A ∪ B  = {1, 2, 3, 4, 5}
A ∩ B  = {3}
A'     = {4, 5}
A − B  = {1, 2}
A △ B  = {1, 2, 4, 5}
A × B  = {(1,3),(1,4),(1,5),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5)}

Power set of {1,2}: [∅, {1}, {2}, {1,2}]
```

---

### Practical 2 — RELATION Class
**File:** `dm_practical2_relation.py`

Represents a relation on set {1..n} using an **n×n adjacency matrix**. Checks all four properties and identifies the relation type.

| Property | Rule |
|----------|------|
| Reflexive | (a,a) ∈ R for all a |
| Symmetric | (a,b) ∈ R → (b,a) ∈ R |
| Anti-symmetric | (a,b) ∈ R ∧ (b,a) ∈ R → a = b |
| Transitive | (a,b) ∈ R ∧ (b,c) ∈ R → (a,c) ∈ R |
| **Equivalence** | Reflexive + Symmetric + Transitive |
| **Partial Order** | Reflexive + Anti-symmetric + Transitive |

**Sample:**
```
Pairs: {(1,1),(2,2),(3,3),(1,2),(2,1)}
  Reflexive: True  |  Symmetric: True
  Transitive: True |  Equivalence Relation: True ✓

Pairs: {(1,1),(2,2),(3,3),(1,2),(1,3),(2,3)}
  Anti-symmetric: True  |  Partial Order: True ✓
```

---

### Practical 3 — Permutations
**File:** `dm_practical3_permutations.py`

Generates permutations both with and without repetition using two approaches each: `itertools` and manual recursive backtracking.

| Type | Formula | Example P(3,2) |
|------|---------|----------------|
| Without repetition | P(n,r) = n!/(n−r)! | 6 arrangements |
| With repetition | nʳ | 9 arrangements |

**Sample:**
```
Elements = [1, 2, 3],  r = 2

Without repetition (P(3,2)=6):
  (1,2) (1,3) (2,1) (2,3) (3,1) (3,2)

With repetition (3²=9):
  (1,1) (1,2) (1,3) (2,1) (2,2) (2,3) (3,1) (3,2) (3,3)
```

---

### Practical 4 — Equation Solver
**File:** `dm_practical4_equation_solver.py`

Solves **x₁ + x₂ + ⋯ + xₙ = C** (C ≤ 10) by brute-force enumeration of all non-negative integer solutions. Validates count against the **Stars & Bars** combinatorial formula.

```
Formula: Number of solutions = C(C+n−1, n−1)
```

**Sample:**
```
n=3, C=4  →  x1 + x2 + x3 = 4

Solutions (15 total):
  (0,0,4)  (0,1,3)  (0,2,2)  (0,3,1)  (0,4,0)
  (1,0,3)  (1,1,2)  ...

Theory C(6,2) = 15  ✓
```

---

### Practical 5 — Polynomial Evaluation
**File:** `dm_practical5_polynomial.py`

Stores polynomial as a coefficient array `[a₀, a₁, ..., aₙ]` where index i = power of x. Supports two evaluation methods:

| Method | Complexity | Description |
|--------|-----------|-------------|
| Direct | O(n²) | Σ aᵢ × xⁱ term by term |
| Horner's | O(n) | Nested multiplication, fewer operations |

Also supports polynomial addition and multiplication.

**Sample:**
```
Coefficients: [2, -3, 0, 5]  →  P(x) = 2 - 3x + 5x³

P(2):  Direct = 2 - 6 + 0 + 40 = 36
       Horner = 36  ✓

(x−1) × (x+1) = x² − 1
```

---

### Practical 6 — Complete Graph Checker
**File:** `dm_practical6_complete_graph.py`

Checks if an undirected graph is a **complete graph Kₙ** — every pair of distinct vertices is connected by exactly one edge.

```
Complete iff: every matrix[i][j] = 1 for all i ≠ j
Expected edges in Kₙ: n(n−1)/2
```

**Sample:**
```
K4 (4 vertices):
  Matrix:       Degree sequence: [3,3,3,3]
  0 1 1 1       Actual edges:    6
  1 0 1 1       Expected (K4):   6
  1 1 0 1       Complete? True ✓
  1 1 1 0

Path P3:  Missing edge (1,3)  →  Complete? False ✗
```

---

### Practical 7 — Directed Graph Degree
**File:** `dm_practical7_digraph.py`

Computes in-degree and out-degree for every vertex of a directed graph and verifies the **Directed Handshaking Lemma**.

```
In-degree  of v  = sum of column v   (edges entering v)
Out-degree of v  = sum of row v      (edges leaving v)

Lemma: Σ in-degree = Σ out-degree = |E|

Special vertices:
  Source   → in-degree  = 0
  Sink     → out-degree = 0
  Isolated → both = 0
```

**Sample:**
```
Edges: 1→2, 1→3, 2→4, 3→4, 4→1

  Vertex │ In-deg │ Out-deg │ Total
  ───────┼────────┼─────────┼──────
       1 │      1 │       2 │     3
       2 │      1 │       1 │     2
       3 │      1 │       1 │     2
       4 │      2 │       1 │     3

  Σin = Σout = |E| = 5  ✓
```

---

## Key Concepts Covered

| Concept | Practicals |
|---------|-----------|
| Set Theory | 1 |
| Relations & Properties | 2 |
| Combinatorics | 3, 4 |
| Sequences & Algebra | 5 |
| Graph Theory | 6, 7 |

---

## Tips

- All menus support `0` to exit back to master launcher.
- Practical 2 has built-in demos — select option 2 to see them without typing pairs.
- Practical 4 gets slow for n > 6 with C = 10 (C¹⁰ iterations). Stay within n ≤ 6.
- Practical 5 stores int-valued coefficients as `int`, floats as `float` automatically.
- Practical 6 auto-generates any Kₙ via option 3 — useful for testing.

---