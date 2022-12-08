# Front Matrix
    # Wall = '#'
    # Player = 'P'
    # Stone = 'O'
    # Skeleton = 'S'
    # Goal = 'G'
# Back Matrix
    # Key = 'k'
    # Lock = 'l'
    # Spike Hole = '.' - ':'
    # Spike = ','

class Level:
    front_matrix = []
    back_matrix = []

    def __init__(self, level_num):
        del self.front_matrix[:]
        del self.back_matrix[:]
        with open(f'levels\level{level_num}.txt', 'r') as f:
            self.moves = f.readline()
        self.moves = int(self.moves)
        with open(f'levels\level{level_num}.txt', 'r') as f:
            temp = f.readline()
            for row in f.read().splitlines():
                self.front_matrix.append(list(row))
                self.back_matrix.append(list(row))
        
        f = ['#', 'P', 'O', 'S', 'G']
        b = ['k', 'l', '.', ':', ',']
        for i in range (0, len(self.front_matrix)):
            for j in range (0, len(self.front_matrix[i])):
                if self.front_matrix[i][j] in b:
                    self.front_matrix[i][j] = ' '
        for i in range (0, len(self.back_matrix)):
            for j in range (0, len(self.back_matrix[i])):
                if self.back_matrix[i][j] in f:
                    self.back_matrix[i][j] = ' '

    def getFrontMatrix(self):
        return self.front_matrix
    def getBackMatrix(self):
        return self.back_matrix
    
    def getPlayerPosition(self):
        for i in range (0, len(self.front_matrix)):
            for j in range (0, len(self.front_matrix[i])):
                if self.front_matrix[i][j] == 'P':
                    return [i, j]


# myLevel = Level(1)
# print(myLevel.moves)
# for i in myLevel.front_matrix:
#     for j in i:
#         print(j, end='')
#     print()
# for i in myLevel.back_matrix:
#     for j in i:
#         print(j, end='')
#     print()
