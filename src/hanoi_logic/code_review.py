
from hanoi_solver import HanoiSolver

disks = 5
solver = HanoiSolver(disks)

solver.solve()
print(solver.get_solution())