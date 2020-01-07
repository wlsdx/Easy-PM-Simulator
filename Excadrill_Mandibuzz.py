from random import randrange
# 252 Atk Jolly Excadrill vs 252HP 88Def Careful(+SpD-SpA) Mandibuzz

#Can Mandibuzz switch in Excadrill(no Swords Dance, no Rock Slide) with more than half HP left?
#Excadrill always uses Iron Head
#Mandibuzz switch in at first turn

#Result:
#try 100000, Mandibuzz wins 41364
#Mandibuzz can stall Excadrill with more than half HP by the chance of about 41%

Head = [118, 120, 121, 123, 124, 126, 127, 129, 130, 132, 133, 135, 136, 138, 139, 141]
HeadCT = [178, 181, 183, 186, 187, 189, 192, 193, 196, 198, 199, 202, 204, 207, 208, 211]
Foul=[240, 243, 246, 249, 252, 255, 256, 259, 262, 265, 268, 271, 274, 277, 280, 283]
FoulCT=[360, 364, 369, 373, 376, 381, 385, 390, 394, 399, 402, 406, 411, 415, 420, 424]

#ExcaHP=361,MandHP=424


############### Assumptions: Before Head pp goes to 0 

def MandStrategy(MandHP):
    if MandHP<=424/2+130:
        return 1#Roost if HP<=50% after this attack
    else:
        return 2#Foul Play if HP

#f=open("Exca_vs_Mand.csv",'w')
MandWin = 0
for i in range(10):#Game loop
    #print('Round %d'%(i+1))
    ExcaHP,MandHP=361,424
    #Take a hit when switch in
    roll=randrange(0, 16)
    if randrange(1, 25) != 1:
        dam=Head[roll]
    else:
        dam=HeadCT[roll]
    MandHP = MandHP - dam
    #print('Excadrill used Iron Head!\nMandibuzz HP %d to %d, loses %.2f%%\n'%(MandHP+dam,MandHP,100*dam/424))
    for t in range(24):#Turn loop. Iron Head PP=24
        #print('Turn %d'%(t+1))
        MandStrgy=MandStrategy(MandHP)
        roll=randrange(0, 16)
        if randrange(1, 25) != 1:
            dam=Head[roll]
        else:
            dam=HeadCT[roll]
        MandHP = MandHP - dam
        #print('Excadrill used Iron Head!\nMandibuzz HP %d to %d, loses %.2f%%\n'%(MandHP+dam,MandHP,100*dam/424))
        if MandHP<1:
            #print('Mandibuzz Fainted! Excadrill HP %d\n'%ExcaHP)
            break
        if randrange(0,10)<3:
            #print('Mandibuzz Flinched!\n')
            continue
        else:
            if MandStrgy == 1:
                rec=min(MandHP + 212, 424)-MandHP
                MandHP = MandHP+rec
                #print('Mandibuzz used Roost! HP %d to %d, gains %.2f%%\n'%(MandHP-rec,MandHP,100*rec/424))
            else: 
                roll=randrange(0, 16)
                if randrange(1, 25) != 1:
                    dam=Foul[roll]
                else:
                    dam=FoulCT[roll]
                ExcaHP = ExcaHP-dam
                #print('Mandibuzz used Foul Play!\nExcadrill HP %d to %d, loses %.2f%%\n'%(ExcaHP+dam,ExcaHP,100*dam/361))
                if ExcaHP<1:
                    #print('Excadrill Fainted! Mandibuzz HP %d\n'%MandHP)
                    MandWin=MandWin+1
                    break
            continue
        #print('Turn 24 over')
        MandWin=MandWin+1
   
    #f.write(str(MandWin)+'\n')
print(MandWin)

