"""
============================================================
DISCRETE MATHEMATICS — MASTER LAUNCHER
All 7 Practicals in One File
============================================================
Run this file to access any practical from one menu.
============================================================
"""

import importlib.util
import os
import sys


PRACTICALS = {
    "1": ("SET Class",                "dm_practical1_set.py"),
    "2": ("RELATION Class",           "dm_practical2_relation.py"),
    "3": ("PERMUTATIONS",             "dm_practical3_permutations.py"),
    "4": ("EQUATION SOLVER",          "dm_practical4_equation_solver.py"),
    "5": ("POLYNOMIAL EVALUATION",    "dm_practical5_polynomial.py"),
    "6": ("COMPLETE GRAPH CHECKER",   "dm_practical6_complete_graph.py"),
    "7": ("DIRECTED GRAPH DEGREE",    "dm_practical7_digraph.py"),
}


def run_practical(filename):
    """Dynamically import and run a practical's menu() function."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_dir, filename)

    if not os.path.exists(path):
        print(f"  ⚠ File not found: {path}")
        return

    spec = importlib.util.spec_from_file_location("practical", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    if hasattr(mod, "menu"):
        mod.menu()
    else:
        print("  ⚠ No menu() function found in this practical.")


def master_menu():
    print("\n" + "═" * 55)
    print("    DISCRETE MATHEMATICS — PRACTICAL LAB")
    print("    B.E. Computer Science & Engineering")
    print("═" * 55)

    while True:
        print("\n  Select a Practical:")
        print("  ┌──────────────────────────────────────────┐")
        for key, (title, _) in PRACTICALS.items():
            print(f"  │  {key}. {title:<38}│")
        print("  │  0. Exit                                 │")
        print("  └──────────────────────────────────────────┘")

        choice = input("\n  Enter choice: ").strip()

        if choice == "0":
            print("\n  Goodbye! Happy coding.\n")
            break
        elif choice in PRACTICALS:
            title, filename = PRACTICALS[choice]
            print(f"\n  Launching: {title}")
            print("  " + "─" * 42)
            run_practical(filename)
        else:
            print("  ❌ Invalid choice. Enter 0–7.")


if __name__ == "__main__":
    master_menu()
