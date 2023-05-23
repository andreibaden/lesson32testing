class Orange:
    def __init__(self, diametr=100, vitamin=1000, cost=0):
        self.__diametr = diametr
        self.__vitamin = vitamin
        self.__cost = cost

    @property
    def diametr(self):
        return self.__diametr

    @property
    def vitamin(self):
        return self.__vitamin

    @property
    def cost(self):
        return self.__cost

    @vitamin.setter
    def vitamin(self, vitamin):
        self.__vitamin = vitamin

    @diametr.setter
    def diametr(self, diametr):
        self.__diametr = diametr

    @cost.setter
    def cost(self, cost):
        self.__cost = cost

    def __str__(self):
        return (f"Orange: diametr = {self.__diametr}, "
                f" vitamin C = {self.__vitamin}, "
                f" cost = {self.__cost}$.")


