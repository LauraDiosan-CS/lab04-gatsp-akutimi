from ga import GA
from utile import readNet,costDrum,readNetFloat


def submeniuGA():
    paramGA={}
    print("Introduceti numarul de cromozomi:")
    popSize=input()
    try:
        popSize=int(popSize)
    except TypeError:
        popSize=10
    paramGA['popSize']=popSize

    print("Introduceti numarul de generatii:")
    noGen = input()
    try:
        noGen = int(noGen)
    except TypeError:
        noGen = 10
    paramGA['noGen'] = noGen

    print("alegeti tipul de evolutie:\n1.Simpla\n2.Elitista\n3.SteadyState")
    FuncEvolutie=input()
    if FuncEvolutie=="1":
        paramGA['FuncEvolutie']='oneGeneration'
    elif FuncEvolutie=="2":
        paramGA['FuncEvolutie']='oneGenerationElitism'
    elif FuncEvolutie=="3":
        paramGA['FuncEvolutie']='oneGenerationSteadyState'
    else:
        paramGA['FuncEvolutie']='oneGeneration'
    return paramGA

def rulareGA(ga):
    allBestPath=[]
    allBestFitnesses = []
    generations = []
    ga.initialisation()
    ga.evaluation()
    bestGen=0
    currentBestChromo=ga.bestChromosome()

    for g in range(ga.getGAparam()['noGen']):
        bestChromo= ga.bestChromosome()
        if bestChromo.fitness<currentBestChromo.fitness:
            currentBestChromo=bestChromo
            bestGen=g
        bestSolX = bestChromo.repres
        allBestPath.append(bestSolX)

        bestSolY = bestChromo.fitness
        allBestFitnesses.append(bestSolY)

        # allAvgFitnesses.append(sum(allPotentialSolutionsY) / len(allPotentialSolutionsY))
        generations.append(g)

        # logic alg
        print("Gen ", g, "-> drum:", allBestPath[g], "cost:", allBestFitnesses[g])
        getattr(ga,ga.getGAparam()['FuncEvolutie'])()

        # ga.oneGeneration()
        # ga.oneGenerationElitism()
        # ga.oneGenerationSteadyState()
    print("Best path:",currentBestChromo.repres,"cost:",currentBestChromo.fitness,"in generation ",bestGen)






def meniuPrincipal():

    iesim=False
    while not iesim:
        print("1.easy\n2.medium\n3.hard\n4.fricker\n5.berlin\n0.Iesire")
        comanda=input()
        if comanda=="0":
            iesim=True
        elif comanda=="1":
            retea=readNet("easy_06_tsp.txt")
            paramProbl={'min': 0, 'max': retea['noNodes']-1, 'function': costDrum, 'noDim': retea['noNodes'], 'retea': retea}
            paramGA=submeniuGA()
            obiectGA=GA(paramGA,paramProbl)
            rulareGA(obiectGA)
        elif comanda=="2":
            retea=readNet("medium_06_tsp.txt")
            paramProbl={'min': 0, 'max': retea['noNodes']-1, 'function': costDrum, 'noDim': retea['noNodes'], 'retea': retea}
            paramGA=submeniuGA()
            obiectGA=GA(paramGA,paramProbl)
            rulareGA(obiectGA)
        elif comanda=="3":
            retea=readNet("hard_06_tsp.txt")
            paramProbl={'min': 0, 'max': retea['noNodes']-1, 'function': costDrum, 'noDim': retea['noNodes'], 'retea': retea}
            paramGA=submeniuGA()
            obiectGA=GA(paramGA,paramProbl)
            rulareGA(obiectGA)
        elif comanda=="4":
            retea=readNet("fricker26.txt")
            paramProbl={'min': 0, 'max': retea['noNodes']-1, 'function': costDrum, 'noDim': retea['noNodes'], 'retea': retea}
            paramGA=submeniuGA()
            obiectGA=GA(paramGA,paramProbl)
            rulareGA(obiectGA)
        elif comanda=="5":
            retea=readNetFloat("berlin.txt")
            paramProbl={'min': 0, 'max': retea['noNodes']-1, 'function': costDrum, 'noDim': retea['noNodes'], 'retea': retea}
            paramGA=submeniuGA()
            obiectGA=GA(paramGA,paramProbl)
            rulareGA(obiectGA)


def main():
    meniuPrincipal()

main()
