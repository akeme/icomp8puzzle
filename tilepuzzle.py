# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

import puzzle 
import sys
import searches

#t=puzzle.TilePuzzle(int(sys.argv[1]))
#t.permute(int(sys.argv[2]))

t=puzzle.TilePuzzle(3)
num = int(raw_input("Qual a quantidade de permutacoes? "))
t.permute(num)

t.printPuzzle()
s=searches.Search(t)


print "Considerando Best First: ", s.bestFirst() 
print "Considerando Busca em Profundidade: ", s.iterativeDeepening()
print "Considerando Busca Gulosa 1: ", s.greedy(0)
print "Considerando Busca Gulosa 2: ", s.greedy(1)
print "Considerando A* 1:", s.aSearch(0)
print "Considerando A* 2:", s.aSearch(1)
