from queue import Empty
from typing import List, Dict

#   A B C D E F
# A 0 1 0 1 1 0
# B 1 0 1 0 0 0
# C 0 1 0 0 1 1
# D 1 0 0 0 1 0
# E 1 0 1 1 0 1
# F 0 0 1 0 0 1

def BFS(graphEx: List[List], Legend: List[str], start: int):
    visited: List = [False] * len(graphEx[0])
    que: List = [start]
    visited[start] = True
    
    
    while que:
        current = que.pop(0)
        print(Legend[current], end=" ")
        
        for i in range(len(graphEx[0])):
            for j in range(len(graphEx[0])):
                if ((graphEx[i][j] == 1) and (not visited[j])):
                    que.append(j)
                    visited[j] = True



if __name__ == '__main__':
    Graph : List[List] = [[0,1,0,1,1,0],
                          [1,0,1,0,0,0],
                          [0,1,0,0,1,1],
                          [1,0,0,0,1,0],
                          [1,0,1,1,0,1],
                          [0,0,1,0,0,1]]

    Legend : List[str] = ["A", "B", "C", "D", "E", "F"]
    
    BFS(Graph, Legend, 0)
