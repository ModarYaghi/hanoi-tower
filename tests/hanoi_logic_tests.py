import unittest
# from src.hanoi_logic.hanoi_solver import HanoiSolver
from hanoi_solver import HanoiSolver


class TestHanoiSolver(unittest.TestCase):
    def test_init_with_negative_num_disks(self):
        with self.assertRaises(ValueError):
            HanoiSolver(-1)

    def test_init_with_zero_num_disks(self):
        solver = HanoiSolver(0)
        self.assertEqual(solver.num_disks, 0)

    def test_init_with_positive_num_disks(self):
        solver = HanoiSolver(3)
        self.assertEqual(solver.num_disks, 3)

    def test_solve_with_zero_num_disks(self):
        solver = HanoiSolver(0)
        solver.solve()
        self.assertEqual(solver.get_solution(), [])

    def test_solve_with_positive_num_disks(self):
        solver = HanoiSolver(3)
        solver.solve()
        solution = solver.get_solution()
        self.assertEqual(len(solution), 7)
        self.assertEqual(solution[0], ("A", "C"))
        self.assertEqual(solution[1], ("A", "B"))
        self.assertEqual(solution[2], ("C", "B"))
        self.assertEqual(solution[3], ("A", "C"))
        self.assertEqual(solution[4], ("B", "A"))
        self.assertEqual(solution[5], ("B", "C"))
        self.assertEqual(solution[6], ("A", "C"))


if __name__ == "__main__":
    unittest.main()
