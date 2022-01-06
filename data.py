from random import random, uniform, choice
from prettytable import PrettyTable
from math import sqrt



import matplotlib.pyplot as plt
"""
Descripción:
Entradas:
Salidas:
"""

"""
Descripción: Esta función genera una lista de cierta cantidad de elementos (especificados por el usuario),
donde dichos elementos van dentro del rango que se le indique.
Entradas:
    -min:       Menor valor posible para el rango
    -max:       Mayor valor posible para el rango
    -samp:      Cantidad de elementos en la lista
Salidas:
    -num:       Lista que contiene los números generados de forma aleatoria
"""
def genRandData(min, max, samp):
    num=[]
    for i in range(samp):
        num.append(uniform(min, max))
    return num

"""
Descripción: Esta función permite obtener el porcentaje de error de un valor experimental en relación con 
su valor teorico.
Entradas:
    -expVal:    Valor experimental obtenido
    -realVal:   Valor teorico
Salidas:
    -porErr:    Porcentaje de error obtenido
"""
def getPorErr(expVal, realVal):
    porErr=str(abs(expVal-realVal)*100/realVal)+"%"
    return porErr


def getProb(benCas,totCas):
    prob=0
    if benCas<totCas:
        prob=benCas/totCas
    return prob

def getProbPor(benCas,totCas):
    probPor=(getProb(benCas,totCas)*100)+"%"
    return probPor

def getComp(benCas,totCas):
    comp=1-getProb(benCas,totCas)
    return comp

def getComp(benCas,totCas):
    comp=str(100-getProb(benCas,totCas)*100)+"%"
    return comp


class Data:
    def __init__(self,information, type):
        self.type=type #Poblacional o muestral
        self.information=sorted(information)
        self.totData=len(information)
        self.totVals=None
        
    def getVals(self):
        vals=[]
        for element in self.information:
            if element not in vals:
                vals.append(element)
        vals.sort()
        self.totVals=len(vals)
        return vals

    def getAbsFreqVals(self):
        vals=self.getVals()
        freqs=[0 for i in range(self.totVals)]
        for element in self.information:
            for j in range(len(vals)):
                if element==vals[j]:
                    freqs[j]+=1
        return freqs
    
    def getRelFreqVals(self):
        freqs=self.getAbsFreqVals()
        relFreqs=[]
        for i in range(len(freqs)):
            relFreqs.append(str(round(freqs[i]*100/self.totData,3))+"%")
        return relFreqs

    """ 
    def fullData(self):
        fullData=self.getVals(),self.getAbsFreqVals(),self.getRelFreqVals()
        return fullData
    """

    def getMaxFreq(self): 
        freqs=self.getAbsFreqVals()
        maxFreq=0

        for i in range(self.totVals):
            if freqs[i]>maxFreq:
                maxFreq=freqs[i]
        return maxFreq

    def getTrend(self):
        freqs=self.getAbsFreqVals()
        vals=self.getVals()
        maxFreq=self.getMaxFreq()       
        trend=[]

        for i in range(self.totVals):
            if freqs[i]==maxFreq:
                trend.append(vals[i])
        
        if len(trend)==1:
            trend=trend[0]

        return trend, maxFreq

    #MOSTRAR DATOS:
    def freqAnal(self):
        vals=self.getVals()
        freqs=self.getAbsFreqVals()
        relFreqs=self.getRelFreqVals()

        res=PrettyTable()    
        res.field_names=["Valores","Frecuencias Absolutas", "Frecuencias Relativas"]
        for i in range(self.totVals):
            res.add_row([vals[i],freqs[i],relFreqs[i]])
        return res


    def saveFreqAnal(self, filename):
        fullData=self.freqAnal().get_string()
        with open(filename,"w") as f:   
            f.write(fullData)
    
    def genHist(self):
        plt.figure(figsize=(8,5))
        plt.bar([str(element) for element in self.getVals()], self.getAbsFreqVals(), color="#0F7564",edgecolor ='black',linewidth=1.5)
        plt.grid(axis='y')
        plt.xlabel("Valores")
        plt.ylabel("Frecuencias absolutas")
        plt.yticks([int for int in range(self.getMaxFreq()+1)])
        plt.title("Analisís de frecuencias para los datos",fontweight ='bold')
    
    def genPieChart(self):
        plt.figure(figsize=(8,5))    
        plt.pie(self.getAbsFreqVals(),labels=[str(element) for element in self.getVals()],autopct='%.2f%%')
        plt.legend(title="Valores suministrados: ")
        plt.title("Digrama de pastel para los datos suministrados",fontweight="bold")
   
        

            
class numData(Data):
    
    def __init__(self, information, type):
        super().__init__(information, type)
    
    def getMin(self):
        return self.information[0]

    def getMax(self):
        return self.information[-1]

    def getFirQuar(self):
        if (self.totData+1)%4==0: #Es multiplo de cuatro 
            Q1=self.information[((self.totData+1)//4)-1]
        else:
            Q1=(self.information[((self.totData+1)//4)]+self.information[((self.totData+1)//4)-1])/2
        return Q1

    def getThirQuar(self):
        if (self.totData+1)%4==0: #Es multiplo de cuatro
            Q3=self.information[3*((self.totData+1)//4)-1]
        else:
            Q3=(self.information[(3*(self.totData+1)//4)]+self.information[(3*(self.totData+1)//4)-1])/2
        return Q3

    def getMed(self):
        med=None
        if self.totData%2!=0: #Impar
            med=self.information[self.totData//2]
        else:
            med=(self.information[self.totData//2]+self.information[(self.totData//2)-1])/2
        return med
    
    def getProm(self):
        sum=0
        for element in self.information:
            sum=sum+element
        prom=sum/self.totData
        return prom

    def getPobVar(self):
        prom=self.getProm()
        sum=0
        for element in self.information:
            sum=sum+(element-prom)**2
        pobVar=sum/self.totData
        return pobVar

    def getPobDev(self):
        return sqrt(self.getPobVar())
    
    def getPobcoefVar(self):
        coefVar=str(self.getPobDev()*100/self.getProm())+"%"
        return coefVar

    def getPobStdVal(self,specVal):
        z=(specVal-self.getProm())/self.getPobDev()
        return z


    def getPMuestVar(self):
        prom=self.getProm()
        sum=0
        for element in self.information:
            sum=sum+(element-prom)**2
        muestVar=sum/(self.totData-1)
        return muestVar
    
    def getMuestDev(self):
        return sqrt(self.getPMuestVar())

    def getMuestcoefVar(self):
        coefVar=str(self.getMuestDev()*100/self.getProm())+"%"
        return coefVar

    def getMuestStdVal(self,specVal):
        z=(specVal-self.getProm())/self.getMuestDev()
        return z

    #MOSTRAR DATOS:

    def fullData(self):
        res=PrettyTable()    
        res.field_names=["Datos","Valor"]
        res.add_row(["Min:",self.getMin()])
        res.add_row(["Max:",self.getMax()])
        res.add_row(["Mod:",self.getTrend()])
        res.add_row(["Prom:",self.getProm()])
        res.add_row(["Q1(aprox):",self.getFirQuar()])
        res.add_row(["Med:",self.getMed()])
        res.add_row(["Q3(aprox):",self.getThirQuar()])
        return res

    def saveFullData(self, filename):
        fullData=self.fullData().get_string()
        with open(filename,"w") as f:   
            f.write(fullData)


    def genPolFreq(self):
        fig=plt.figure(figsize=(8,5))
        plt.plot(self.getVals(),self.getAbsFreqVals() ,"bo--")
        plt.grid()
        plt.xlabel("Valores")
        plt.ylabel("Frecuencias absolutas")
        plt.xticks(self.getVals())
        plt.yticks([int for int in range(self.getMaxFreq()+1)])
        plt.title("Poligono de frecuencias para los datos",fontweight ='bold')
    
    def genVBoxPlot(self):
        fig=plt.figure(figsize=(8,5))
        plt.boxplot(self.information)
        plt.yticks([self.getMin(),self.getFirQuar(),self.getMed(),self.getThirQuar(),self.getMax()])
        plt.grid(axis="y")

inf=[1.2, 7, 8, 1.2,7,7,8,9,10,11]
typ=1

m=numData( inf, typ)
print(m.information)
"""m.genHist()
m.genPolFreq()
m.genPieChart()
m.genVBoxPlot()

plt.show()"""
print(m.fullData())
m.saveFullData("RESULTADOS")


