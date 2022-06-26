import sys
from operator import mul


class Cpf:
    def __init__(self,cpf:str, dv:int):
        self.cpf = cpf
        self.dv = dv
        self.getDigits()
    
    def getDigits (self):
        return list(map(int,filter(lambda x:x.isdecimal(),self.cpf )))

    def dotProd (self, v1:list[int], v2:list[int]):
        return sum(map(mul, v1, v2))

    def areValidDigits (self):
        cpf1 = self.getDigits()
        dv2 = self.dotProd(cpf1,self.cpf_aux)
        result = dv2 % 11
        dv2 = 0 if result <= 1 else 11 - result
        self.cpf_aux_2 = list(range(11,1,-1))
        cpf1.append(dv2)
        dv1 = self.dotProd(cpf1,self.cpf_aux_2)
        result = dv1 % 11
        dv1 = 0 if result <= 1 else 11 - result
        return (dv2*10 + dv1 == self.dv)