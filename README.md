# Python_AI_Connect4

Technology & Frameworks: Python, Artificial Intelligence, Monte Carlo Tree Search (MCTS), Alpha-Beta/Minimax. 

1. Programmed a connect-4 game that a human can play against an AI agent (MCTS or Alpha-Beta).  
2. The game layout in constructed in a matrix format of M*N rows and columns which are initially empty and built on with 1’s and 2’s indicating player one, and player two respectively as the players play the game. 
3. Players can place an connect-4 disc onto the matrix, and see if the current game state is in a win state based on the longest connected run of pieces each player possesses. 
4. The methods check for disc placement in horizontal, vertical, and straight line wins within the game based on the connect-4 rules and return a boolean value depending on win/lose.
5. Performed a study to search for the ideal variables for an effective Connect-4 game and to maximise the winning percentage.
6. Game parameters which include the game depth, rollout count, and the time were modified to analyse and enhance the overall performance of the algorithm’s.
7. The winning percentage for Alpha-Beta/MiniMax works significantly better at a depth of 4 or 5 as it can explore more state space and choose the optimal move. However, as the depth of the game increases the search of the algorithm has increased causing a trade-off between win efficiency and execution time. 
8. The MCTS algorithm worked better when the rollout, and the time were increased causing an increase in its win percentage. 
