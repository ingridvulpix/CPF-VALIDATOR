import sys
from operator import mul
import random
from random import randint

class Cpf:
    def __init__(self,cpf:str, dv:int):
        self.cpf = cpf
        self.dv = dv
        self.cpf_aux = list(range(10,1,-1))
        self.cpf_aux_2 = list(range(11,1,-1))
        self.getDigits()
    
    def getDigits (self):
        return list(map(int,filter(lambda x:x.isdecimal(),self.cpf )))

    def dotProd (self, v1:list[int], v2:list[int]):
        return sum(map(mul, v1, v2))
    
    def generate_cpf(self):
        self.cpf = list(map(lambda x:str(random.randint(0,9)),range(9)))
        self.areValidDigitsCpf(True)
        output_dv = str(self.dv)
        output_dv = '0'+output_dv[:] if len(output_dv) == 1 else output_dv #add leading 0 if dv2=0
        valid_cpf = ("".join(map(str,self.cpf)))+'-'+(output_dv)
        return valid_cpf

    def areValidDigitsCpf (self,generate_random:bool):
        cpf1 = self.getDigits()
        dv2 = self.dotProd(cpf1,self.cpf_aux)
        result = dv2 % 11
        dv2 = 0 if result <= 1 else 11 - result
        cpf1.append(dv2)
        dv1 = self.dotProd(cpf1,self.cpf_aux_2)
        result = dv1 % 11
        dv1 = 0 if result <= 1 else 11 - result
        self.dv = dv2*10 + dv1 if generate_random == True else self.dv
        return (dv2*10 + dv1 == self.dv)