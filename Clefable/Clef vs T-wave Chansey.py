from random import randrange
#f=open('clef vs chansey.txt','a')
for para in xrange(280,300):
    ChanseyWin=0
    for i in xrange(10000):
        ClefHP,TossPP,BoiledPP=394,32,16
        while TossPP>0:
            ClefHP=ClefHP-100
            TossPP=TossPP-1
            if ClefHP<1:
                break
            if randrange(1,5)!=1 and BoiledPP>0 and ClefHP<para:
                ClefHP=min(ClefHP+197,394)
                BoiledPP=BoiledPP-1
            ClefHP=min(394,ClefHP+24)
        if ClefHP<1:
            ChanseyWin=ChanseyWin+1
    print para,ChanseyWin
#    f.write(str(ClefHP)+'\t'+str(TossPP)+'\t'+str(BoiledPP)+'\t'+str(t)+'\t'+str(result)+'\n')
#f.close()
#Print(Best to use a health bar) everyturn result to see if the strategy is proper
