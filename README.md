# Tower of Hanoi Iterative Solver 🗼

A lightweight Python script to solve the classic Tower of Hanoi mathematical puzzle using an optimal, non-recursive iterative approach. 

## 🛠️ Technologies Used
- **Python 3:** Handles array manipulation, state logging, and cyclic parity logic.
- **Data Structures:** Utilizes dynamic lists for stack operations (`.append()`, `.pop()`) and string formatting for state output.

## 🗂️ Project Structure
- **`hanoi_solver.py`**: The main executable script containing the core algorithm, rod state tracking, and test cases.

## 📊 Core Features
The solver calculates the total minimum moves (`2**N - 1`) and alternates between two primary operations:

- **`hanoi_solver()`**: Computes $2^N - 1$ moves and tracks state transitions across `left`, `middle`, and `right` rods.
- **Odd Moves (1, 3, 5, ...):** Cycles Disk 1 based on total disk count parity:
  - **Odd Total Disks:** `left` → `right` → `middle` → `left`
  - **Even Total Disks:** `left` → `middle` → `right` → `left`
- **Even Moves (2, 4, 6, ...):** Executes the single valid move between the two rods that do **not** contain Disk 1.
- **State Logging:** Captures formatted rod states at each step and returns a clean, multiline string via `.strip()`.

## 🚀 How to Run
1. Clone the repository to your local machine:
   ```bash
   git clone [https://github.com/ahmadbiko/tower-of-hanoi-iterative-solver.git](https://github.com/ahmadbiko/tower-of-hanoi-iterative-solver.git)
