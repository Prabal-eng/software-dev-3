import tkinter as tk
from tkinter import ttk, messagebox
import random
import time

class SudokuSolverGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku Solver & Generator")
        self.master.geometry("720x980")
        self.master.resizable(False, False)

        self.style = ttk.Style()
        self.style.theme_use('clam')

        self.cells = {}
        self.original_cells = set()
        self.create_gui()

    def create_gui(self):
        main_frame = ttk.Frame(self.master, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Title
        title_label = ttk.Label(main_frame, text="Sudoku Solver & Generator", font=('Arial', 18, 'bold'))
        title_label.pack(pady=10)

        # Create input grid
        input_frame = ttk.Frame(main_frame, padding="5")
        input_frame.pack(padx=10, pady=10)

        for row in range(9):
            for col in range(9):
                cell = ttk.Entry(input_frame, width=3, font=('Arial', 18), justify='center')
                cell.grid(row=row, column=col, padx=1, pady=1)
                self.cells[(row, col)] = cell

                # Add thicker borders
                if col % 3 == 0 and col != 0:
                    cell.grid(padx=(3, 1))
                if row % 3 == 0 and row != 0:
                    cell.grid(pady=(3, 1))

        # Create buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=10)

        solve_button = ttk.Button(button_frame, text="Solve", command=self.solve_sudoku)
        solve_button.pack(side=tk.LEFT, padx=5)

        generate_button = ttk.Button(button_frame, text="Generate New Puzzle", command=self.generate_puzzle)
        generate_button.pack(side=tk.LEFT, padx=5)

        clear_button = ttk.Button(button_frame, text="Clear", command=self.clear_grid)
        clear_button.pack(side=tk.LEFT, padx=5)

        # Difficulty slider for generation
        self.difficulty_var = tk.IntVar(value=30)
        difficulty_frame = ttk.Frame(main_frame)
        difficulty_frame.pack(pady=10)
        ttk.Label(difficulty_frame, text="Generation Difficulty:").pack(side=tk.LEFT)
        difficulty_slider = ttk.Scale(difficulty_frame, from_=20, to=60, orient=tk.HORIZONTAL,
                                      variable=self.difficulty_var, length=200)
        difficulty_slider.pack(side=tk.LEFT, padx=10)
        ttk.Label(difficulty_frame, textvariable=self.difficulty_var).pack(side=tk.LEFT)

        # Speed slider for visualization
        self.speed_var = tk.DoubleVar(value=0.05)
        speed_frame = ttk.Frame(main_frame)
        speed_frame.pack(pady=10)
        ttk.Label(speed_frame, text="Solving Speed:").pack(side=tk.LEFT)
        speed_slider = ttk.Scale(speed_frame, from_=0, to=0.1, orient=tk.HORIZONTAL,
                                 variable=self.speed_var, length=200)
        speed_slider.pack(side=tk.LEFT, padx=10)
        ttk.Label(speed_frame, text="Fast").pack(side=tk.LEFT)
        ttk.Label(speed_frame, text="Slow").pack(side=tk.RIGHT)

        # Create status label
        self.status_var = tk.StringVar()
        self.status_var.set("Enter a Sudoku puzzle, generate a new one, or solve!")
        status_label = ttk.Label(main_frame, textvariable=self.status_var, font=('Arial', 10))
        status_label.pack(pady=5)

    def clear_grid(self):
        for cell in self.cells.values():
            cell.delete(0, tk.END)
            cell.configure(style='TEntry')
        self.original_cells.clear()
        self.status_var.set("Grid cleared. Enter a new puzzle or generate one.")

    def get_puzzle(self):
        puzzle = []
        for row in range(9):
            puzzle_row = []
            for col in range(9):
                value = self.cells[(row, col)].get()
                puzzle_row.append(int(value) if value.isdigit() else 0)
            puzzle.append(puzzle_row)
        return puzzle

    def set_puzzle(self, puzzle):
        for row in range(9):
            for col in range(9):
                value = puzzle[row][col]
                self.cells[(row, col)].delete(0, tk.END)
                if value != 0:
                    self.cells[(row, col)].insert(0, str(value))
                    if (row, col) in self.original_cells:
                        self.cells[(row, col)].configure(style='Original.TEntry')
                    else:
                        self.cells[(row, col)].configure(style='Solved.TEntry')
                else:
                    self.cells[(row, col)].configure(style='TEntry')

    def is_valid(self, puzzle, row, col, num):
        # Check row
        if num in puzzle[row]:
            return False

        # Check column
        if num in [puzzle[i][col] for i in range(9)]:
            return False

        # Check 3x3 box
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if puzzle[i][j] == num:
                    return False

        return True

    def solve(self, puzzle):
        for row in range(9):
            for col in range(9):
                if puzzle[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(puzzle, row, col, num):
                            puzzle[row][col] = num
                            self.set_puzzle(puzzle)
                            self.master.update()
                            time.sleep(self.speed_var.get())

                            if self.solve(puzzle):
                                return True

                            puzzle[row][col] = 0
                            self.set_puzzle(puzzle)
                            self.master.update()
                            time.sleep(self.speed_var.get())

                    return False
        return True

    def solve_sudoku(self):
        puzzle = self.get_puzzle()
        self.status_var.set("Solving...")
        self.master.update()

        if self.solve(puzzle):
            self.status_var.set("Sudoku solved successfully!")
        else:
            self.status_var.set("No solution exists for this puzzle.")
            messagebox.showinfo("No Solution", "This Sudoku puzzle has no valid solution.")

    def generate_puzzle(self):
        self.clear_grid()
        self.status_var.set("Generating new puzzle...")
        self.master.update()

        # Generate a solved puzzle
        puzzle = [[0 for _ in range(9)] for _ in range(9)]
        self.solve(puzzle)

        # Remove numbers to create the puzzle
        cells = [(row, col) for row in range(9) for col in range(9)]
        to_remove = 81 - self.difficulty_var.get()
        for _ in range(to_remove):
            if not cells:
                break
            row, col = random.choice(cells)
            cells.remove((row, col))
            backup = puzzle[row][col]
            puzzle[row][col] = 0

            # Check if the puzzle still has a unique solution
            copy_puzzle = [row[:] for row in puzzle]
            if not self.has_unique_solution(copy_puzzle):
                puzzle[row][col] = backup

        self.set_puzzle(puzzle)
        self.original_cells = {(row, col) for row in range(9) for col in range(9) if puzzle[row][col] != 0}
        self.status_var.set("New puzzle generated. Solve it or generate another!")

    def has_unique_solution(self, puzzle):
        solutions = [0]
        def solve_count(puz):
            if solutions[0] > 1:
                return
            for row in range(9):
                for col in range(9):
                    if puz[row][col] == 0:
                        for num in range(1, 10):
                            if self.is_valid(puz, row, col, num):
                                puz[row][col] = num
                                solve_count(puz)
                                puz[row][col] = 0
                        return
            solutions[0] += 1
        solve_count(puzzle)
        return solutions[0] == 1

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolverGenerator(root)

    # Define styles for different cell states
    style = ttk.Style()
    style.configure('TEntry', font=('Arial', 18))
    style.configure('Original.TEntry', foreground='blue', font=('Arial', 18, 'bold'))
    style.configure('Solved.TEntry', foreground='green', font=('Arial', 18))

    root.mainloop()
