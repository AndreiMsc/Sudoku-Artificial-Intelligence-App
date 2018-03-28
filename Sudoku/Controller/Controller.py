class Controller:

    def __init__(self,problem):
        self.__problem=problem

    def BFS(self, root):
        q = [root]
        while len(q) > 0:
            currentState = q.pop(0)
            if self.__problem.isok(currentState.getValues()[-1]):
                return currentState
            q = q + self.__problem.expand(currentState)

    def BestFS(self, root):
        visited = []
        toVisit = [root]
        while len(toVisit) > 0:
            node = toVisit.pop(0)
            visited = visited + [node]
            if self.__problem.isok(node.getValues()[-1]):
                return node
            aux = []
            for x in self.__problem.expand(node):
                if x not in visited:
                    aux.append(x)
            aux = [[x, self.__problem.heuristics(x)] for x in aux]
            aux.sort(key=lambda x: x[1])
            aux = [x[0] for x in aux]
            toVisit = aux[:] + toVisit