from random import randint, seed
from utile import generateARandomPermutation



# permutation-based representation
class Chromosome:
    def __init__(self, problParam=None):
        self.__problParam = problParam  # problParam has to store the number of nodes/cities
        self.__repres = generateARandomPermutation(self.__problParam['noDim'])
        self.__fitness = 0.0

    @property
    def repres(self):
        return self.__repres

    @property
    def fitness(self):
        return self.__fitness

    @repres.setter
    def repres(self, l=[]):
        self.__repres = l

    @fitness.setter
    def fitness(self, fit=0.0):
        self.__fitness = fit

    @staticmethod
    def pozitiePermutare(lista,val):
        if val >= len(lista):
            return None
        else:
            for i in range(len(lista)):
                if lista[i]==val:
                    return i

    def crossover(self, c):
        # order XO
        pos1 = randint(-1, self.__problParam['noDim'] - 1)
        pos2 = randint(-1, self.__problParam['noDim'] - 1)
        if pos2 < pos1:
            pos1, pos2 = pos2, pos1
        k = 0
        newrepres = self.__repres[pos1: pos2]
        for el in c.__repres[pos2:] + c.__repres[:pos2]:
            if el not in newrepres:
                if len(newrepres) < self.__problParam['noDim'] - pos1:
                    newrepres.append(el)
                else:
                    newrepres.insert(k, el)
                    k += 1

        offspring = Chromosome(self.__problParam)
        offspring.repres = newrepres
        return offspring
        # operatori topologici
        # #incrucisare ciclica
        # k=0
        # newrepres=[None]*self.__problParam['noDim']
        # p1=self.__repres
        # p2=c.__repres
        # while None in newrepres and k<self.__problParam['noDim']:
        #     prim=p1[k]
        #     newrepres[k]=p1[k]
        #     nou=p2[Chromosome.pozitiePermutare(p1,prim)]
        #     while nou!=prim:
        #         newrepres[nou]=p1[nou]
        #         nou=p2[Chromosome.pozitiePermutare(p1,nou)]
        #     newrepres[nou] = p1[nou]
        #     while k<self.__problParam['noDim'] and newrepres[k] is not None:
        #         k+=1
        #     sav=p1
        #     p1=p2
        #     p2=sav
        # offspring = Chromosome(self.__problParam)
        # offspring.repres = newrepres
        # return offspring

    def mutation(self):
        # # insert mutation
        # pos1 = randint(0, self.__problParam['noDim'] - 1)
        # pos2 = randint(0, self.__problParam['noDim'] - 1)
        # if (pos2 < pos1):
        #     pos1, pos2 = pos2, pos1
        # el = self.__repres[pos2]
        # del self.__repres[pos2]
        # self.__repres.insert(pos1 + 1, el)

        # inversion
        pos1 = randint(0, self.__problParam['noDim'] - 1)
        pos2 = randint(0, self.__problParam['noDim'] - 1)
        if pos2 < pos1:
            pos1, pos2 = pos2, pos1
        while pos2>pos1:
            sav=self.__repres[pos1]
            self.__repres[pos1]=self.__repres[pos2]
            self.__repres[pos2]=sav
            pos1+=1
            pos2-=1


if __name__=="__main__":
    c1=Chromosome({"noDim":9})
    # c1.repres=[0,1,2,3,4,5,6,7,8]
    c2 = Chromosome({"noDim": 9})
    # c2.repres=[8,2,6,7,1,5,4,0,3]
    c3=c1.crossover(c2)
    print(c1,c2,c3)