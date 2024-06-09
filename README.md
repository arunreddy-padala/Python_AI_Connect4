# Connect4_Python_AI

This project presents an interactive Connect-4 game where a human player can compete against an advanced AI agent. The game utilizes two sophisticated AI algorithms: Monte Carlo Tree Search (MCTS) and Alpha-Beta/Minimax. Developed in Python, this application offers a deep dive into artificial intelligence and game theory, providing insights into algorithm efficiency and strategy optimization in game environments.

Technologies and Frameworks: Python, Artificial Intelligence, Monte Carlo Tree Search (MCTS), Alpha-Beta/Minimax

Game Mechanics:
- Game Board: Implemented as an MxN matrix, which begins empty and is filled with 1s (Player One) and 2s (Player Two) as the game progresses.
- Win Detection: The game checks for horizontal, vertical, and diagonal connections to determine the winner, returning a boolean outcome based on the current state of the board.
  
Features:
- AI Agents: Includes two types of AI opponents:
- Alpha-Beta/Minimax Algorithm: Optimized for strategic depth, performing better at depths of 4 or 5, allowing it to explore more state space and select optimal moves.
- Monte Carlo Tree Search (MCTS): Improved performance with increased rollouts and extended computation time, enhancing the probability of winning through more thorough exploration.
- Performance Analysis: Conducted detailed studies to determine optimal game settings and parameters to maximize AI performance and efficiency.
- Dynamic Play: Players can adjust game parameters like depth, rollout count, and decision time to explore different strategic outcomes.
  
Results and Findings:
- Alpha-Beta/Minimax: Demonstrated significant improvement in winning percentages at optimal depths, though deeper searches increased execution time.
- MCTS: Showed enhanced winning percentages with increased rollouts and longer decision times, indicating a balance between computational demands and gameplay performance.
