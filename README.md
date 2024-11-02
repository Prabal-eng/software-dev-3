# Sudoku Solver & Generator

## Overview

The **Sudoku Solver & Generator** is a Python-based desktop application that provides users with the tools to generate, solve, and customize Sudoku puzzles. This app features an intuitive user interface, allowing users to either enter their Sudoku puzzles or generate new ones at various difficulty levels. It also offers a visualization option to watch the solving process in real-time.

## Features

- **Generate Sudoku Puzzles**: Generates new puzzles with adjustable difficulty, providing an endless supply of Sudoku challenges.
- **Solve Existing Puzzles**: Users can enter a puzzle manually and use the solver feature to find a solution.
- **Real-Time Solving Visualization**: Allows users to watch the solving process step-by-step, with an adjustable speed slider to control the pace.
- **User-Friendly Interface**: Clear and easy-to-navigate GUI with well-labeled buttons, sliders, and entry fields.
- **Error Messages for Invalid Puzzles**: Notifies users if the entered puzzle has no solution, ensuring they don't spend time on unsolvable puzzles.

## What I Learned

This project helped me enhance my skills in several areas:
- **GUI Development with Tkinter**: Implemented an interactive user interface using Tkinter widgets such as Labels, Entry fields, Buttons, and Sliders. Designed the layout for clarity and ease of use.
- **Backtracking Algorithm for Sudoku Solving**: Utilized a recursive backtracking approach to solve Sudoku puzzles, handling constraint checks for each cell to ensure valid entries.
- **Puzzle Generation and Difficulty Adjustment**: Generated solvable Sudoku puzzles by selectively removing numbers from a solved grid and ensuring only one unique solution exists. Implemented a difficulty slider to adjust the number of empty cells.
- **Visualization with Adjustable Speed**: Enabled real-time visualization of the solving process with a speed control feature, making the application more engaging and educational.
- **Input Validation**: Added checks for valid entries in each cell and appropriate messages for unsolvable puzzles.

## Installation

1. **Requirements**:
   - Python 3.x
   - Tkinter (typically comes pre-installed with Python)

2. **Installation**:
   - Clone this repository:
     ```bash
     git clone <repository-url>
     ```
   - Run the `sudoku_solver_generator.py` script:
     ```bash
     python sudoku_solver_generator.py
     ```

## Usage

1. **Input a Puzzle**: Manually enter a puzzle in the grid, and click **Solve** to find the solution.
2. **Generate a New Puzzle**: Click **Generate New Puzzle** to get a fresh Sudoku puzzle.
   - Use the **Generation Difficulty** slider to set the puzzle's complexity.
3. **Clear the Grid**: Click **Clear** to reset the grid.
4. **Adjust Solving Speed**: Use the **Solving Speed** slider to control the visualization speed, from slow (0.1s) to fast (instant).

## Example Usage

1. Set the desired difficulty using the **Generation Difficulty** slider.
2. Click **Generate New Puzzle**. A puzzle appears on the grid.
3. Click **Solve** to see the solution in real-time. Adjust the **Solving Speed** to control the visualization pace.

## Future Enhancements

- Implement a timer for solving puzzles, allowing users to track their solve times.
- Add a hint feature that provides possible values for a selected cell.
- Improve the puzzle generator to support more complex difficulty levels (e.g., advanced or expert).
- Add themes to change the app's appearance.
