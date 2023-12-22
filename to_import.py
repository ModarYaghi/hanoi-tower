import src.hanoi_logic.hanoi_solver as hs

solver = hs.HanoiSolver(3)
solver.solve()

print(solver.get_solution())


