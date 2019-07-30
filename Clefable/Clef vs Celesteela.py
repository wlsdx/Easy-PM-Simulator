from random import randrange
# python2.7

# 252+Def Cosmic Clef vs 248HP 104Def 156SpD Relaxed Cele

# ClefStrategy:Soft boiled when HP<tFunc(HP,Def(,pp of both sides)),Cosmic*6,calm mind*6,moonblast.
# ClefStrategyOne:Soft boiled on otherwise-fainted turn(ignoring CT),i.e. when ClefHP<=min(Slam[ClefDef + 1][15]
# ClefStrategyTwo:Soft boiled on otherwise-possibly-fainted turn(ignoring CT),i.e. when ClefHP<=max(Slam[ClefDef + 1][15]
# ClefStrategyThree:Soft boiled if HP<40% or sth and Def at +1 or sth

# CeleStrategy:Heavy Slam.

Slam = [[230, 234, 236, 240, 240, 242, 246, 248, 252, 254, 258, 260, 264, 266, 270, 272],
        [152, 156, 158, 158, 162, 162, 164, 168, 168, 170, 170, 174, 176, 176, 180, 182],
        [116, 116, 120, 120, 120, 122, 122, 126, 126, 128, 128, 132, 132, 134, 134, 138],
        [92, 92, 96, 96, 96, 98, 98, 102, 102, 102, 104, 104, 104, 108, 108, 110],
        [78, 78, 78, 80, 80, 80, 84, 84, 84, 86, 86, 86, 90, 90, 90, 92],
        [66, 68, 68, 68, 72, 72, 72, 72, 74, 74, 74, 74, 78, 78, 78, 80],
        [60, 60, 60, 62, 62, 62, 62, 66, 66, 66, 66, 68, 68, 68, 68, 72],
        [60, 60, 60, 62, 62, 62, 62, 66, 66, 66, 66, 68, 68, 68, 68, 72]]
# Slam[0~6]=ClefDef[0~6] damage;Slam[7] for ClefStrategy calculation
SlamCT = [344, 348, 354, 356, 362, 366, 368, 374, 378, 380, 386, 390, 392, 398, 402, 408]
MBlast = [166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196]  # At +6


def ClefStrategy(ClefHP, ClefDef, ClefSpA):
    if ClefHP <= Slam[ClefDef + 1][15]:  # Boiled Point Needed!?!?!?
        return 1  # Soft Boiled
    elif ClefDef < 6:
        return 2  # Cosmic Power
    elif ClefSpA < 6:
        return 3  # Calm Mind
    else:
        return 4  # Moonblast


# Assumptions:Slam pp goes to 0 earlier than ClefSpA reaches +6 (proved)
# Cele faint in three +6 MBlast.(True unless small rolls and a double protect.But useless because of the last assumption)

f=open("Clef vs Celesteela.txt",'w')
for n in xrange(16,17):  # Slam pp=n
    CeleWin = 0
    for i in xrange(100000):
        ClefHP, ClefDef, ClefSpA, ifBoiled = 394, 0, 0, 0  # Def,SpA:Stage(0~6)
        x = 0  # If x=3,Celesteela fainted
        for t in xrange(n):
            ClefStrgy = ClefStrategy(ClefHP, ClefDef, ClefSpA)
            if ClefStrgy == 1:
                ClefHP = min(ClefHP + 197, 394)
            elif ClefStrgy == 2:
                ClefDef = ClefDef + 1
            elif ClefStrgy == 3:
                ClefSpA = ClefSpA + 1
            else:
                x = x + 1
                if x == 3:
                    break
            if randrange(1, 25) != 1:
                ClefHP = ClefHP - Slam[ClefDef][randrange(0, 16)]
            else:
                ClefHP = ClefHP - SlamCT[randrange(0, 16)]
            if ClefHP < 1:
                break
            ClefHP = min(394, ClefHP + 24) #leftover recovery
        # n-1-t=Slam pp left
        if ClefHP < 1:
            CeleWin = CeleWin + 1
        f.write(str(CeleWin)+'\n')
    print CeleWin
f.close()

# Print(Best to use a health bar) every turn result to see if the strategy is proper
