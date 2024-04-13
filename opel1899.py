class trougao:
    def __init__ (self, a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def Izbir(self):
        return (self.a+self.b+self.c)
Tr1 = trougao (1,2,3)
tr1 = Tr1.Izbir ()
Tr2 = trougao (12,2,31)
tr2 = Tr2.Izbir ()
Tr3 =  trougao (10,5,3)
tr3 = Tr3.Izbir ()
print(max(tr1,tr2,tr3))
print(min(tr1,tr2,tr3))
