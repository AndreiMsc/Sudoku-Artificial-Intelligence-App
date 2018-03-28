from Sudoku.Controller.Controller import Controller
from Sudoku.Problem.Problem import Problem
from time import time

class UI:

    def __init__(self,filename):
        self.__filename=filename
        self.__problem=Problem(self.__filename)
        self.__ctrl=Controller(self.__problem)

    def printMainMenu(self):
        s=''
        s+="0-exit \n"
        s+="1-find a path with BFS\n"
        s+="2-find a path with BestFS/GBFS\n"
        print(s)

    def findPathBFS(self):
        startClock=time()
        print(str(self.__ctrl.BFS(self.__problem.getRoot())))
        print('execution time=',time()-startClock,"seconds")

    def findPathBestFS(self):
        startClock=time()
        print(str(self.__ctrl.BestFS(self.__problem.getRoot())))
        print('execution time=',time()-startClock,"seconds")

    def run(self):
        print("Hello and wellcome to my SUDOKU Application. The problem solves the sudoku using 'Best First Search and GBFS algortihms\n")
        print("The puzzles are in the text files in the Repository packages.\n")
        runM=True
        while runM:
            self.printMainMenu()
            try:
                command=int(input(">>"))
                if command==0:
                    print("Thank you for using my application! Check out my other applications on www.githup.com/AndreiMsc !")
                    runM=False
                elif command==1:
                    self.findPathBFS()
                elif command==2:
                    self.findPathBestFS()
            except:
                print('Invalid command! Try again..')