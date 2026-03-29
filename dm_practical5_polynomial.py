"""
============================================================
PRACTICAL 5 — POLYNOMIAL EVALUATION
Discrete Mathematics | Python Implementation
============================================================
Features:
  - Store polynomial coefficients in an array
  - Polynomial: P(x) = a0 + a1*x + a2*x^2 + ... + an*x^n
  - Evaluate P(x) for given x using:
      (a) Direct method (sum of terms)
      (b) Horner's method (efficient, O(n))
  - Display polynomial in readable form

Sample Input/Output:
  Degree  : 3
  Coeffs  : [2, -3, 0, 5]    → 2 - 3x + 0x² + 5x³
  Evaluate at x=2:
    Direct  : 2 - 6 + 0 + 40 = 36
    Horner  : 36
============================================================
"""


class Polynomial:
    def __init__(self, coefficients):
        """
        coefficients: list [a0, a1, a2, ..., an]
          where a0 is the constant term and an is the leading coefficient.
        """
        self.coeffs = coefficients  # index i → coefficient of x^i
        self.degree = len(coefficients) - 1

    # ── String representation ─────────────────────────────────
    def __str__(self):
        """Return human-readable polynomial string."""
        if not self.coeffs:
            return "0"

        terms = []
        for i, a in enumerate(self.coeffs):
            if a == 0:
                continue
            # Build term string
            if i == 0:
                term = str(a)
            elif i == 1:
                term = f"{a}x" if a != 1 else "x"
            else:
                term = f"{a}x^{i}" if a != 1 else f"x^{i}"

            terms.append(term)

        if not terms:
            return "0"

        # Join: first term as-is, subsequent with sign
        result = terms[0]
        for t in terms[1:]:
            if t.startswith("-"):
                result += f" - {t[1:]}"
            else:
                result += f" + {t}"
        return result

    # ── Method 1: Direct evaluation ───────────────────────────
    def evaluate_direct(self, x):
        """
        P(x) = Σ a_i * x^i
        Straightforward term-by-term summation.
        """
        total = 0
        steps = []
        for i, a in enumerate(self.coeffs):
            term_val = a * (x ** i)
            total += term_val
            steps.append(f"({a}×{x}^{i}={term_val})")
        return total, steps

    # ── Method 2: Horner's method ─────────────────────────────
    def evaluate_horner(self, x):
        """
        Horner's Method: reduces multiplications.
        P(x) = a0 + x(a1 + x(a2 + x(... + x*an)))
        O(n) multiplications instead of O(n^2).
        """
        result = 0
        for a in reversed(self.coeffs):   # start from highest degree
            result = result * x + a
        return result

    # ── Full evaluation report ────────────────────────────────
    def evaluate_report(self, x):
        direct_val, steps = self.evaluate_direct(x)
        horner_val = self.evaluate_horner(x)
        print(f"\n  Polynomial : P(x) = {self}")
        print(f"  Degree     : {self.degree}")
        print(f"  Coefficients (a0..an): {self.coeffs}")
        print(f"\n  Evaluating at x = {x}:")
        print(f"  Direct method  : {' + '.join(steps)}")
        print(f"                   = {direct_val}")
        print(f"  Horner's method: {horner_val}")
        match = "✓ Both methods agree" if direct_val == horner_val else "✗ Mismatch!"
        print(f"  Verification   : {match}")
        return direct_val

    # ── Evaluate for multiple x values (table) ────────────────
    def evaluate_table(self, x_values):
        print(f"\n  P(x) = {self}")
        print(f"\n  {'x':>6}  │  {'P(x)':>12}")
        print("  " + "─" * 24)
        for x in x_values:
            val = self.evaluate_horner(x)
            print(f"  {x:>6}  │  {val:>12}")

    # ── Polynomial addition ───────────────────────────────────
    def add(self, other):
        """Return self + other as a new Polynomial."""
        max_len = max(len(self.coeffs), len(other.coeffs))
        c1 = self.coeffs + [0] * (max_len - len(self.coeffs))
        c2 = other.coeffs + [0] * (max_len - len(other.coeffs))
        return Polynomial([a + b for a, b in zip(c1, c2)])

    # ── Polynomial multiplication ─────────────────────────────
    def multiply(self, other):
        """Return self × other as a new Polynomial."""
        result = [0] * (len(self.coeffs) + len(other.coeffs) - 1)
        for i, a in enumerate(self.coeffs):
            for j, b in enumerate(other.coeffs):
                result[i + j] += a * b
        return Polynomial(result)


# ── Input helper ──────────────────────────────────────────────
def input_polynomial(label=""):
    tag = f" ({label})" if label else ""
    print(f"\n  Enter polynomial{tag}:")
    deg = int(input("  Degree of polynomial: "))
    print(f"  Enter {deg + 1} coefficients a0, a1, ..., a{deg}:")
    coeffs = []
    for i in range(deg + 1):
        c = float(input(f"    a{i} (coefficient of x^{i}): "))
        # Store as int if whole number
        coeffs.append(int(c) if c == int(c) else c)
    return Polynomial(coeffs)


# ── Menu ──────────────────────────────────────────────────────
def menu():
    print("\n" + "═" * 55)
    print("   DISCRETE MATHEMATICS — POLYNOMIAL EVALUATION")
    print("═" * 55)

    while True:
        print("""
┌─────────────────────────────────────────┐
│         POLYNOMIAL EVALUATION MENU      │
├─────────────────────────────────────────┤
│  1. Evaluate polynomial at x            │
│  2. Evaluate over a range (table)       │
│  3. Add two polynomials                 │
│  4. Multiply two polynomials            │
│  5. Run built-in demos                  │
│  0. Exit                                │
└─────────────────────────────────────────┘""")
        choice = input("  Enter choice: ").strip()

        if choice == "0":
            print("  Exiting POLYNOMIAL module.")
            break

        elif choice == "1":
            p = input_polynomial()
            try:
                x = float(input("  Evaluate at x = "))
                x = int(x) if x == int(x) else x
                p.evaluate_report(x)
            except ValueError:
                print("  ⚠ Invalid x.")

        elif choice == "2":
            p = input_polynomial()
            raw = input("  Enter x values (space-separated): ").split()
            try:
                xs = [int(v) if float(v) == int(float(v)) else float(v) for v in raw]
                p.evaluate_table(xs)
            except ValueError:
                print("  ⚠ Invalid input.")

        elif choice == "3":
            print("  ── Polynomial Addition ──")
            p1 = input_polynomial("P")
            p2 = input_polynomial("Q")
            result = p1.add(p2)
            print(f"\n  P(x) = {p1}")
            print(f"  Q(x) = {p2}")
            print(f"  P+Q  = {result}")

        elif choice == "4":
            print("  ── Polynomial Multiplication ──")
            p1 = input_polynomial("P")
            p2 = input_polynomial("Q")
            result = p1.multiply(p2)
            print(f"\n  P(x) = {p1}")
            print(f"  Q(x) = {p2}")
            print(f"  P×Q  = {result}")

        elif choice == "5":
            print("\n  ── DEMO 1: P(x) = 2 - 3x + 5x³ ──")
            p = Polynomial([2, -3, 0, 5])
            p.evaluate_report(2)
            p.evaluate_table([-2, -1, 0, 1, 2])

            print("\n\n  ── DEMO 2: (x+1)(x-1) = x²-1 ──")
            p1 = Polynomial([-1, 1])   # x - 1
            p2 = Polynomial([1, 1])    # x + 1
            prod = p1.multiply(p2)
            print(f"  (x-1)(x+1) = {prod}")
            prod.evaluate_table([0, 1, 2, 3])

        else:
            print("  ❌ Invalid choice.")


if __name__ == "__main__":
    menu()
