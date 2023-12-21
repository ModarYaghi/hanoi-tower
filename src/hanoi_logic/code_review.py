
from hanoi_solver import HanoiSolver

disks = 4
solver = HanoiSolver(disks)

solver.solve()
print(solver.get_solution())