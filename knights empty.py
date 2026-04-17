# Solves the tasks with a knight on the chessboard:
# 1) shortest path of a knight from the starting position on the chessboard to all other positions
# 2) knight's tour, where the knight visits all squares of the chessboard exactly once

import Stack

class KnightSolution:
    def __init__(self, n):
        self.n = n  # size of the chessboard
        self.board = [[-1 for _ in range(n)] for _ in range(n)]
        self.predecessors = [[(-1,-1) for _ in range(n)] for _ in range(n)] # predecessor of each position
        self.moves = [] # list of possible knight moves
        self.biggestD = 1

    def solve_shortest_paths(self, start):
        """
        Solves task 1: Finds the shortest path from the start position to all other squares using BFS.
        Fills self.board with distances and self.predecessors with previous positions.
        """
        q = Stack.Queue()
        q.enqueue(start)
        self.board[start[0]][start[1]] = 0
        while not q.is_empty():
            prevMove = q.dequeue()
            self.posMoves(prevMove)
            for move in self.moves:
                if self.board[move[0]][move[1]] == -1:
                    self.board[move[0]][move[1]] = self.board[prevMove[0]][prevMove[1]] + 1
                    q.enqueue(move)
                    self.predecessors[move[0]][move[1]] = prevMove

    
    def solve_knight_tour(self, start, one_solution=True):
        """
        Solves task 2: Finds a knight's tour from the start position using DFS.
        Updates self.board with move numbers and self.predecessors with the path.
        If one_solution is True, stops after finding the first valid tour.
        Prints all found solutions (matrices board and predecessors).
        """
        self.board[start[0]][start[1]] = 0
        self.solveTour(start, one_solution)

    def solveTour(self, position, oneSolution):
        if self.board[position[0]][position[1]] == self.n**2 - 1:
            self.print_board()
            print()
            return oneSolution

        self.posMoves(position)

        for move in self.moves:
            if self.board[move[0]][move[1]] == -1:
                self.board[move[0]][move[1]] = self.board[position[0]][position[1]] + 1
                self.predecessors[move[0]][move[1]] = position

                if self.solveTour(move, oneSolution):
                    return True

                self.board[move[0]][move[1]] = -1
                self.predecessors[move[0]][move[1]] = (-1,-1)
        return False


    def posMoves(self, position):
        out = []
        for i in range(-1,2,2):
            for j in range(-1,2,2):
                possiblePosI = (position[0] + 1*i, position[1] + 2*j)
                possiblePosJ = (position[0] + 2*i, position[1] + 1*j)
                if self.isValid(possiblePosI[0], possiblePosI[1]):
                    out.append(possiblePosI)
                if self.isValid(possiblePosJ[0], possiblePosJ[1]):
                    out.append(possiblePosJ)
        self.moves = out

    def isValid(self, row, column):
        return 0 <= row < self.n and 0 <= column < self.n

    def print_board(self):
        """ Prints the current state of the board (distances or move numbers). """
        mostDigits = self.biggestNum()
        for i in range(self.n):
            for j in range(self.n):
                txt = str(self.board[i][j]).rjust(mostDigits)
                print(txt, end=" ")
            print()

    def biggestNum(self):
        out = -1
        for i in self.board:
            for j in i:
                if len(str(j)) > out:
                    out = len(str(j))
        return out

    def print_predecessors(self):
        """Prints the matrix of predecessors for each position"""
        for i in range(self.n):
            for j in range(self.n):
                print(self.predecessors[i][j], end=" ")
            print()

    def get_distance(self, position):
        """Returns the distance or move number at a given position"""
        return self.board[position[0]][position[1]]

    def get_path(self, position):
        """Reconstructs the path from the start to the given position using predecessors
        Returns the list of states on the path from the start to the given position (inclusive)
        """
        path = []

        while position != (-1,-1):
            path.append(position)
            position = self.predecessors[position[0]][position[1]]

        path.reverse()
        return path
# --- Testing functions ---

def test_shortest_paths():
    n = 5
    knight_solution = KnightSolution(n)
    knight_solution.solve_shortest_paths((0,0))

    print("Distances from (0,0) to other positions:")
    knight_solution.print_board()
    print("\nPredecessors:")
    knight_solution.print_predecessors()

    end = (1, 1)
    print(f"\nPath from (0,0) to {end}:")
    print("Distance:", knight_solution.get_distance(end))
    print("Path:", knight_solution.get_path(end))

''' Solution:

Distances from (0,0) to other positions:
 0  3  2  3  2
 3  4  1  2  3
 2  1  4  3  2
 3  2  3  2  3
 2  3  2  3  4

 Predecessors: # may look different deppending on the ordering of moves
(-1, -1) (1, 3) (2, 1) (2, 4) (1, 2)
(0, 2) (2, 3) (0, 0) (2, 1) (0, 2)
(1, 2) (0, 0) (3, 4) (4, 2) (1, 2)
(4, 2) (1, 2) (4, 0) (2, 1) (4, 2)
(2, 1) (3, 3) (2, 1) (3, 1) (2, 3)

Path from (0,0) to (1,1):
distance:  4
path:  [(0, 0), (2, 1), (4, 2), (2, 3), (1, 1)]
'''

def test_tour():

    n = 5
    knight_solution = KnightSolution(n)
 
    print("Path from (0,0) to other positions in the matrix:")
    knight_solution.solve_knight_tour((0,0))

    end = (4, 1)
    print(f"\nPath from (0,0) to {end}:")
    print("Move number:", knight_solution.get_distance(end))
    print("Path:", knight_solution.get_path(end))

''' One of possible solutions (you may get another one):

Path from (0,0) to other positions in the matrix:
 0  5 14  9 20
13  8 19  4 15
18  1  6 21 10
 7 12 23 16  3
24 17  2 11 22

Predecessors: # may look different deppending on the ordering of moves
(-1, -1) (1, 3) (1, 0) (1, 1) (1, 2)
(3, 1) (3, 0) (2, 0) (3, 4) (0, 2)
(4, 1) (0, 0) (0, 1) (0, 4) (0, 3)
(2, 2) (4, 3) (4, 4) (1, 4) (4, 2)
(3, 2) (3, 3) (2, 1) (2, 4) (2, 3)

Path from (0,0) to (4,1):
distance:  17
path:  [(0, 0), (2, 1), (4, 2), (3, 4), (1, 3), (0, 1), (2, 2), (3, 0), (1, 1), (0, 3), (2, 4), (4, 3), (3, 1), (1, 0), (0, 2), (1, 4), (3, 3), (4, 1)]

'''

# --- Main entry point ---

if __name__ == "__main__":
    test_shortest_paths()
    test_tour()
    """
        test_shortest_paths()
    
        print("\n" + "=" * 50 + "\n")
        
        test_tour()        
    """





