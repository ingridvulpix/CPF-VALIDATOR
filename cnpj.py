import sys
from operator import mul
import random


class Cnpj:
    def __init__(self,cnpj:str, dv:int):
        self.cnpj = cnpj
        self.dv_cnpj = dv
        self.cnpj_aux = [5,4,3,2,9,8,7,6,5,4,3,2]
        self.cnpj_aux_2 = [6,5,4,3,2,9,8,7,6,5,4,3,2]
        self.getDigits()
    
    def getDigits (self):
        return list(map(int,filter(lambda x:x.isdecimal(),self.cnpj )))

    def dotProd (self, v1:list[int], v2:list[int]):
        return sum(map(mul, v1, v2))

    def generate_cnpj(self):#FIXME cnpj has A LOT of leading 0, needs a different generator
        self.cnpj = list(map(lambda x:str(random.randint(0,9)),range(12)))
        self.areValidDigitsCnpj(True)
        output_dv = str(self.dv_cnpj)
        output_dv = '0'+output_dv[:] if len(output_dv) == 1 else output_dv #add leading 0 if dv2=0
        valid_cnpj = ("".join(map(str,self.cnpj)))+'-'+(output_dv)
        return valid_cnpj

    def areValidDigitsCnpj(self, generate_random:bool):
        cnpj1 = self.getDigits()
        dv2 = self.dotProd(cnpj1,self.cnpj_aux)
        result = dv2 % 11
        dv2 = 0 if result <= 1 else 11 - result
        cnpj1.append(dv2)
        dv1 = self.dotProd(cnpj1,self.cnpj_aux_2)
        result = dv1 % 11
        dv1 = 0 if result <= 1 else 11 - result
        self.dv_cnpj = dv2*10 + dv1 if generate_random == True else self.dv_cnpj
        return (dv2*10 + dv1 == self.dv_cnpj)
