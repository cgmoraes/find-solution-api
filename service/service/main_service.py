import time
from loguru import logger
from service.constants import mensagens
import math


class Equation():

    def __init__(self):
        self.roots = []
        self.response = {}

    def executar_rest(self, coefficients):

        logger.debug(mensagens.INICIO_SOLUCAO)
        start_time = time.time()

        self.encontrar_raizes(coefficients['a'], coefficients['b'], coefficients['c'])

        logger.debug(mensagens.FIM_SOLUCAO)
        logger.debug(f"Obtencao de todas as raizes em {time.time()-start_time}")

        return self.response

    def encontrar_raizes(self, a, b, c):
        logger.debug('Iniciando a solucao...')

        if a != 0:
            self.bhaskara(a,b,c)  
        else:
            x = (-c)/b
            self.roots.append("{:.2f}".format(x))
        
        if len(self.roots) > 1:
            self.response['x1'] = self.roots[0]
            self.response['x2'] = self.roots[1]
        else:
            self.response['x'] = self.roots[0]

    def bhaskara(self, a, b, c):
        delta = (b**2)-(4*a*c)

        if delta >= 0:
            x1 = (-b + math.sqrt(delta))/(2*a)
            x2 = (-b - math.sqrt(delta))/(2*a)

            self.roots.append("{:.2f}".format(x1))
            self.roots.append("{:.2f}".format(x2))
        else:
            delta = -delta
            realPart = (-b)/(2*a)
            imagPart =  "± {:.2f}i".format(math.sqrt(delta)/(2*a))

            x = "{:.2f} ".format(realPart) + imagPart

            self.roots.append(x)