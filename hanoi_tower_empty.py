from typing import List

class HanoiTower:
    """
    Object-oriented implementation of the Tower of Hanoi puzzle.
    """
    def __init__(self, n: int) -> None:
        """
        Initialize towers and start the solution.

        Tower A contains n disks (largest at bottom),
        towers B and C are empty.

        Initializes a step counter and prints the initial state.
        Then starts the recursive algorithm to solve the puzzle.
        """
        self.step = 0
        self.a = []
        self.b = []
        self.c = []
        self.maxLength = n
        for i in range(1,n+1):
            self.a.insert(0,i)
        self.print_towers()
        self._move(n,self.a,self.b,self.c)

    def _print_tower(self, tower: List[int]) -> str:
        """
        Prints one tower as a string of disk numbers, using '_' for empty level.
        """
        out = ""
        for d in tower:
            out += str(d)
        out = out.ljust(self.maxLength, "_")
        return ":" + out

    def print_towers(self) -> None:
        """
        Prints the step number and current state of all three towers.
        """
        out = f"{self.step}" + self._print_tower(self.a) + self._print_tower(self.b) + self._print_tower(self.c)
        print(out)

    def _move(self, n, tower_from, tower_to, tower_aux) -> None:
        """
        Recursive function to move 'n' disks from t_from to t_to
        using t_aux as auxiliary tower.
        """
        if n == 1:
            self.step +=1
            tower_to.append(tower_from.pop())
            self.print_towers()
            return
        self._move(n - 1, tower_from, tower_aux, tower_to)
        self.step += 1
        tower_to.append(tower_from.pop())
        self.print_towers()
        self._move(n - 1, tower_aux, tower_to, tower_from)


if __name__ == "__main__":
    for n in range(1, 6):
        print()
        HanoiTower(n)

    print("test ok")