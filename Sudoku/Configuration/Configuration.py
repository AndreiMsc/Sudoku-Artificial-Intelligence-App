class Configuration:

    def __init__(self,positions):
        self.__size=len(positions)
        self.__values=positions[:]

    def getSize(self):
        return self.__size

    def getValues(self):
        return self.__values[:]

    def nextConfig(self,j):
        nextC=[]
        for x in range(j+1,self.__size):
            aux=self.__values[:]
            if aux[j]<aux[x]:
                aux[j],aux[x]=aux[x],aux[j]
                nextC.append(Configuration(aux))
        return nextC

    def __str__(self):
        return str(self.__values)

    def __eq__(self,other):
        if not isinstance(other,Configuration):
            return False
        if self.__size!=other.getSize():
            return False
        for i in range(self.__size):
            if self.__values[i]!=other.getValues()[i]:
                return False
        return True