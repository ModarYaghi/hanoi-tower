import unittest
from hanoi_solver import HanoiSolver


class TestHanoiSolver(unittest.TestCase):
    def test_initialization(self):
        solver = HanoiSolver(3)
        self.assertEqual(solver.num_disks, 3)
        self.assertEqual(solver.moves, [])

    def test_solve(self):
        solver = HanoiSolver(3)
        solver.solve()
        # The number of moves for a 3 disk puzzle should be 2^n - 1 = 7
        self.assertEqual(len(solver.moves), 7)

    def test_moves(self):
        solver = HanoiSolver(1)
        solver.solve()
        # For a single disk, there should be one move from "A" to "C"
        self.assertEqual(solver.moves, [("A", "C")])

    def test_no_disks(self):
        solver = HanoiSolver(0)
        solver.solve()
        # If there are no disks, there should be no moves
        self.assertEqual(solver.moves, [])


if __name__ == "__main__":
    unittest.main()
