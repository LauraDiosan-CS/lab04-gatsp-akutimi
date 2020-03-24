from random import randint
from chromozom import Chromosome
from utile import costDrum


class GA:  # GENETIC ALGORITHM!!!
    def __init__(self, param=None, problParam=None):
        self.__param = param
        self.__problParam = problParam
        self.__population = []

        # initialise de GA parameters
        # gaParam = {'popSize': 10, 'noGen': 3, 'pc': 0.8, 'pm': 0.1}
        # problem parameters
        # problParam = {'min': MIN, 'max': MAX, 'function': fcEval, 'noDim': noDim, 'noBits': 8}
        # function == fitness function
        # nodim == dimensiunea unui cromozom
        # noBits == noDim in binary repr.

    @property
    def population(self):
        return self.__population

    def initialisation(self):
        for _ in range(0, self.__param['popSize']):
            c = Chromosome(self.__problParam)
            self.__population.append(c)

    def getGAparam(self):
        return self.__param

    def getProbParam(self):
        return self.__problParam

    def evaluation(self):
        for c in self.__population:
            c.fitness = self.__problParam['function'](self.__problParam['retea']['mat'],c.repres)

    def bestChromosome(self):
        best = self.__population[0]
        for c in self.__population:
            if c.fitness < best.fitness:
                best = c
        return best

    def worstChromosome(self):
        best = self.__population[0]
        for c in self.__population:
            if c.fitness > best.fitness:
                best = c
        return best

    def selection(self):
        pos1 = randint(0, self.__param['popSize'] - 1)
        pos2 = randint(0, self.__param['popSize'] - 1)
        if self.__population[pos1].fitness < self.__population[pos2].fitness:
            return pos1
        else:
            return pos2

    def oneGeneration(self):
        newPop = []
        for _ in range(self.__param['popSize']):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            newPop.append(off)
        self.__population = newPop
        self.evaluation()

    def oneGenerationElitism(self):
        newPop = [self.bestChromosome()]
        for _ in range(self.__param['popSize'] - 1):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            newPop.append(off)
        self.__population = newPop
        self.evaluation()

    def oneGenerationSteadyState(self):
        for _ in range(self.__param['popSize']):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            off.fitness = self.__problParam['function'](self.__problParam['retea']['mat'],off.repres)
            worst = self.worstChromosome()
            if off.fitness < worst.fitness:
                i=self.__population.index(worst)
                self.__population[i]=off

