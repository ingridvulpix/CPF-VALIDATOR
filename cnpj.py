import sys
from operator import mul


class Cnpj:
    def __init__(self,cnpj:str, dv:int):
        self.cnpj = cnpj
        self.dv = dv
        self.cnpj_aux = [5,4,3,2,9,8,7,6,5,4,3,2]
        self.cnpj_aux_2 = [6,5,4,3,2,9,8,7,6,5,4,3,2]
        self.getDigits()
    
    def getDigits (self):
        return list(map(int,filter(lambda x:x.isdecimal(),self.cnpj )))

    def dotProd (self, v1:list[int], v2:list[int]):
        return sum(map(mul, v1, v2))

    def areValidDigits (self):
        cnpj1 = self.getDigits()
        dv2 = self.dotProd(cnpj1,self.cnpj_aux)
        result = dv2 % 11
        dv2 = 0 if result <= 1 else 11 - result
        cnpj1.append(dv2)
        dv1 = self.dotProd(cnpj1,self.cnpj_aux_2)
        result = dv1 % 11
        dv1 = 0 if result <= 1 else 11 - result
        print (dv2*10 + dv1 == self.dv)
