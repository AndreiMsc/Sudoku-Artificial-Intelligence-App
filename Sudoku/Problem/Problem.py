from Sudoku.Configuration.Configuration import Configuration
from Sudoku.State.State import State
import math

class Problem:

    def __init__(self,filename):
        self.__filename=filename
        self.__initialConfig=self.readFromFile(self.__filename)
        self.__initialState=State()
        self.__initialState.setValues([self.__root])

    def expand(self,currentState):
        myList=[]
        currentConfig=currentState.getValues()[-1]
        for j in range(currentConfig.getSize()):
            for x in currentConfig.nextConfig(j):
                myList.append(currentState+x)
        return myList

    def getNewRoot(self):
        return self.__root

    def getRoot(self):
        return self.__initialState

    def getInitialConfig(self):
        return self.__initialConfig

    def readFromFile(self, filename):
        f = open(filename, "r")
        m = f.readline().strip("\n").split(" ")
        n = int(m[0])
        self.__n=n
        list=[0]*(n+1)
        Matrix = [[0 for x in range(n)] for y in range(n)]
        for i in range(0, n):
            line = f.readline().strip("\n").split(" ")
            for j in range(0, n):
                a = int(line[j])
                Matrix[i][j] = a
                if Matrix[i][j]!=0:
                    list[Matrix[i][j]]=list[Matrix[i][j]]+1
        root=[]
        for y in range(1,n+1):
            for z in range(list[y],n):
                root.append(y)
        self.__root=Configuration(root)
        self.__numbers = []
        for i in range(1, self.__n + 1):
            self.__numbers.append(i)
        return Matrix


    def isok(self, state1):
        Matrix = [[0 for x in range(self.__n)] for y in range(self.__n)]
        state=state1.getValues()
        q = 0;
        for i in range(0, self.__n):
            for j in range(0, self.__n):

                if self.__initialConfig[i][j] == 0:
                    Matrix[i][j] = state[q]
                    q = q + 1
                else:
                    Matrix[i][j] = self.__initialConfig[i][j]
        self.__matrix=Matrix
        for i in range(0, self.__n):
            x = [0] * self.__n
            for j in range(0, self.__n):
                x[Matrix[i][j] - 1] = x[Matrix[i][j] - 1] + 1
                if x[Matrix[i][j] - 1] > 1:
                    return False
        for j in range(0, self.__n):
            x = [0] * self.__n
            for i in range(0, self.__n):
                x[Matrix[i][j] - 1] = x[Matrix[i][j] - 1] + 1
                if x[Matrix[i][j] - 1] > 1:
                    return False
        for i in range(0, self.__n, int(math.sqrt(self.__n))):
            for j in range(0, self.__n, int(math.sqrt(self.__n))):
                if self.missingNrInBlock(i, j, Matrix) != set():
                    return False
        return True

    def missingNrInBlock(self, row, column, matrix):
        l = set(self.__numbers)
        sqr = math.sqrt(self.__n)
        for i in range(int(int(row / sqr) * sqr), int((int(row / sqr) + 1) * sqr)):
            for j in range(int(int(column / sqr) * sqr), int((int(column / sqr) + 1) * sqr)):
                if matrix[i][j] in l:
                    l.remove(matrix[i][j])
        return l

    def heuristics(self,state1):
        Matrix = [[0 for x in range(self.__n)] for y in range(self.__n)]
        state=state1.getValues()
        l=self.__root.getSize()
        q=0
        for i in range(l):
            for i in range(0, self.__n):
                x = [0] * self.__n
                for j in range(0, self.__n):
                    x[self.__matrix[i][j] - 1] = x[self.__matrix[i][j] - 1] + 1
                    if x[Matrix[i][j] - 1] != 1:
                        l=l+1

            for j in range(0, self.__n):
                x = [0] * self.__n
                for i in range(0, self.__n):
                    x[self.__matrix[i][j] - 1] = x[self.__matrix[i][j] - 1] + 1
                    if x[Matrix[i][j] - 1] != 1:
                        l=l+1
            for i in range(0, self.__n, int(math.sqrt(self.__n))):
                for j in range(0, self.__n, int(math.sqrt(self.__n))):
                    if self.missingNrInBlock(i, j, self.__matrix) != set():
                        l=l+1
            return l