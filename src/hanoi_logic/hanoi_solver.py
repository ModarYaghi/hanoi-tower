from typing import List, Tuple


class HanoiSolver:
    """
    HanoiSolver class to solve Tower of Hanoi puzzle.

    Contains methods to initialize the puzzle with number of disks,
    recursively solve the puzzle by moving disks between pegs,
    and track the list of moves made.

    The recursive _solve_recursive method implements the logic
    to move disks from source to destination peg using the
    auxiliary peg, by recursively moving smaller stacks of disks.
    """

    def __init__(self, num_disks: int) -> None:
        """
            Initializes the HanoiSolver with the given number of disks to solve for.
        Validates num_disks is a non-negative integer.
        Sets the num_disks attribute to track the number of disks.
        Initializes empty moves list to track sequence of moves made during the solution.
        """
        if num_disks < 0:
            raise ValueError("Number of disks must be non-negative.")
        elif num_disks == 0:
            print("There are no disks to move.")

        self.num_disks = num_disks
        self.moves: List[Tuple[str, str]] = []

    def solve(self) -> None:
        """
        Calls the _solve_recursive method to solve the Tower of Hanoi puzzle
        with the initialized number of disks, passing in the 3 pegs "source",
        "auxiliary", "destination" as the source, auxiliary and destination pegs.
        """
        self._solve_recursive(self.num_disks, "A", "B", "C")

    def _move_disk(self, source: str, destination: str) -> None:
        """
        Appends the disk move from source peg to destination peg to
        the moves list to track sequence of moves made during
        the solution.
        """
        self.moves.append((source, destination))

    def _solve_recursive(
        self, n: int, source: str, auxiliary: str, destination: str
    ) -> None:
        """
        Recursively solves Tower of Hanoi puzzle by moving disks from source to destination using auxiliary peg
        Base case is when n == 1, only need to move single disk from source to destination
        Otherwise, recursively move n-1 disks from source to auxiliary, move bottom disk from source to destination,
        then recursively move n-1 disks from auxiliary to destination
        """
        if n == 0:
            # self._move_disk(source, destination)
            # Base case: no disk to move, so retrun immediately
            return
        self._solve_recursive(n - 1, source, destination, auxiliary)
        self._move_disk(source, destination)
        self._solve_recursive(n - 1, auxiliary, source, destination)


    def get_solution(self) -> List[Tuple[str, str]]:
        """
        Returns the list of disk move tuples representing the
        sequence of moves made during the recursive solution.
        This provides the full trace of the disk movements
        required to solve the Tower of Hanoi puzzle for the
        given number of disks.
        """
        return self.moves
