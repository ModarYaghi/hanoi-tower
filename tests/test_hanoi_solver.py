from pathlib import Path
import pytest
import sys


sys.path.append(str(Path(__file__).parent.parent / "src"))

from hanoi_logic.hanoi_solver import HanoiSolver

def test_hanoi_solver_init():
    # Test initialization with valid number of disks
    solver = HanoiSolver(3)
    assert solver.num_disks == 3
    assert solver.moves == []

    # Test initialization with zero disks
    solver = HanoiSolver(0)
    assert solver.num_disks == 0
    assert solver.moves == []

    # Test initialization with negative number of disks
    with pytest.raises(ValueError):
        HanoiSolver(-1)

def test_hanoi_solver_solve():
    # Test solving the puzzle with 3 disks
    solver = HanoiSolver(3)
    solver.solve()
    assert solver.moves == [("A", "C"), ("A", "B"), ("C", "B"), ("A", "C"), ("B", "A"), ("B", "C"), ("A", "C")]

    # Test solving the puzzle with 0 disks
    solver = HanoiSolver(0)
    solver.solve()
    assert solver.moves == []

def test_hanoi_solver_get_solution():
    # Test getting the solution after solving the puzzle
    solver = HanoiSolver(3)
    solver.solve()
    solution = solver.get_solution()
    assert solution == [("A", "C"), ("A", "B"), ("C", "B"), ("A", "C"), ("B", "A"), ("B", "C"), ("A", "C")]

    # Test getting the solution without solving the puzzle
    solver = HanoiSolver(3)
    solution = solver.get_solution()
    assert solution == []
