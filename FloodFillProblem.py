from typing import List

def validToFill(Graph, row, col, x, y, preC, postC) -> bool:
        if (x<0 or x>=row or y<0 or y>=col or Graph[x][y] != preC or Graph[x][y] == postC):
            return False
        return True


def BFS(Graph, row: int, col: int, x:int, y:int, preColor: int, postColor: int):
    start = [x,y]
    que=[start]
    
    while que:
        current = que.pop(0)
        posX = current[0]
        posY = current[1]
            
        for i in range(-1,2,1):
            for j in range(-1,2,1):
                if i != j:
                    if validToFill(Graph, row, col, (posX + i), (posY + j), preColor, postColor):
                        Graph[posX + i][posY + j] = postColor
                    
                        que.append([(posX+i), (posY+j)])
                    
    output(Graph, row, col)
                    
def output(Graph, row, col):
    for i in range(row):
        for j in range(col):
            print(Graph[i][j], end=" ")
            
        print("\n")


if __name__ == '__main__':
    Graph: List[List] = [[1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,0,0],
            [1,0,0,1,1,0,1,1],
            [1,2,2,2,2,0,1,0],
            [1,1,1,2,2,0,1,0],
            [1,1,1,2,2,2,2,0],
            [1,1,1,1,1,2,1,1],
            [1,1,1,1,1,2,2,1]]
    
    row : int = len(Graph)
    col : int = len(Graph[0])
    
    x : int = 4
    y: int = 4
    preColor : int = 2
    postColor : int = 3
    
    BFS(Graph, row, col, x, y, preColor, postColor)