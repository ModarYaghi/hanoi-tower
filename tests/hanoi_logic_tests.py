"""
Import unittest module for creating unit tests.
"""
import unittest
# import sys
# sys.path.append(r"C:/Users/fmny/hanoi_solver/src/hanoi_logic")
# from src.hanoi_logic.hanoi_solver import HanoiSolver
# from hanoi_solver import HanoiSolver
import src


# class TestHanoiSolver(unittest.TestCase):
#     """
#     Unit tests for the HanoiSolver class.
#     """

#     def test_init_with_negative_num_disks(self):
#         """
#         Test case to verify that initializing HanoiSolver with a negative number of disks raises
#         a ValueError.
#         """
#         with self.assertRaises(ValueError):
#             src.HanoiSolver(-1)

    # def test_init_with_zero_num_disks(self):
    #     """
    #     Test case to verify the initialization of HanoiSolver with zero number of disks.
    #     """
    #     solver = HanoiSolver(0)
    #     self.assertEqual(solver.num_disks, 0)

    # def test_init_with_positive_num_disks(self):
    #     """
    #     Test case to verify the initialization of HanoiSolver with a positive number of disks.
    #     """
    #     solver = HanoiSolver(3)
    #     self.assertEqual(solver.num_disks, 3)

    # def test_solve_with_zero_num_disks(self):
    #     """
    #     Test case to verify the behavior of the solve method when the number of disks is zero.
    #     """
    #     solver = HanoiSolver(0)
    #     solver.solve()
    #     self.assertEqual(solver.get_solution(), [])

    # def test_solve_with_positive_num_disks(self):
    #     """
    #     Test case to verify the solution for solving the Hanoi Tower puzzle
    #     with a positive number of disks.
    #     """
    #     solver = HanoiSolver(3)
    #     solver.solve()
    #     solution = solver.get_solution()
    #     self.assertEqual(len(solution), 7)
    #     self.assertEqual(solution[0], ("A", "C"))
    #     self.assertEqual(solution[1], ("A", "B"))
    #     self.assertEqual(solution[2], ("C", "B"))
    #     self.assertEqual(solution[3], ("A", "C"))
    #     self.assertEqual(solution[4], ("B", "A"))
    #     self.assertEqual(solution[5], ("B", "C"))
    #     self.assertEqual(solution[6], ("A", "C"))


if __name__ == "__main__":
    unittest.main()
