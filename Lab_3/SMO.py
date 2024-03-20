from math import factorial

class SMO:

    '''
        #Интeнсивность (вызов в минуту, Лямбда)
        Intensity #Проверка на 0

        #Время обслуживания 1 заявки
        ServiceTime #Проверка на 0

        #интенсивность обслуживания заявок (мю)
        IntensityService  #Проверка на 0

        #Вероятность обслуживания заявки
        ProbabilityService

        #Время простоя
        DownTime

        #Вероятность отказа
        ProbabilityFault

        #Абсолютная пропускная способность (А)
        Bandwidth

        #Интенсивность потока заявок
        MultIntensity

        #Среднее число занятых каналов
        AverageChannel

        #Относительная пропускная способность
        RelativeBandwidth

        #Время ожидания в очереди
        WaitTime

        #среднее число заявок в СМО
        Lsmo

        #Средняя длина очереди
        QueueLength

        #Вероятность образования очереди
        ProbabilityQueue

        #Среднее время нахождения в СМО
        SMOTime
        
        #Статична ли СМО. False - если очередь будет стремиться в бесконечность
        IsStatic
    '''

    def __init__(self, intensity, serviceTime, intensityService=0):

        self.Intensity=intensity
        self.ServiceTime=serviceTime
        if intensityService==0:
            self.IntensityService=1/self.ServiceTime
        else:
            self.IntensityService=intensityService

    def SingleChannelWithFail(self):
       #Вероятность обслуживания заявки
        self.ProbabilityService=self.IntensityService/(self.Intensity+self.IntensityService)
        #Время простоя
        self.DownTime=1/self.Intensity
        #Вероятность отказа в обслуживании
        self.ProbabilityFault=1-self.ProbabilityService
        #Пропускная способность
        self.Bandwidth=self.Intensity*self.ProbabilityService
        
    def SingleChannelWithQueue(self, len):
        p=self.Intensity/self.IntensityService
        
        if p==1:
            p_0=1/(len+2)
        else:
            p_0=(1-p)/(1-(p**(len+2)))
       #Вероятность обслуживания заявки
        self.ProbabilityService=self.Intensity/(self.Intensity+self.IntensityService)
        self.ProbabilityFault=(p**(len+1))*p_0
        self.RelativeBandwidth=1-self.ProbabilityFault
        self.AverageChannel=self.RelativeBandwidth*self.Intensity
        if p==1:
                self.QueueLength=(len*(len+1))/(2*(len+2))
        else:
             self.QueueLength=(p**2)*(1-(p**len)*(len-len*p+1))/((1-p)**2)
        self.WaitTime=self.QueueLength/self.Intensity
        self.Lsmo=1+self.QueueLength
        if p!=1:
            self.SMOTime=self.Lsmo/self.Intensity
        else:
            self.SMOTime=(len+1)/(2*self.IntensityService)
            
    def SingleChannelWithQueueWhithoutLen(self):
        p=self.Intensity/self.IntensityService
        if p<1:
            self.IsStatic=True
         
            self.QueueLength=(p**2)/(1-p)
            self.WaitTime=self.QueueLength/self.Intensity
            self.Lsmo=(p)/(1-p)
            self.SMOTime=self.Lsmo/self.Intensity
        else:
            self.IsStatic=False
            
    def MultiChannelWithFail(self, ChannelCount):
        #Вероятность обслуживания заявки
        self.MultIntensity=self.Intensity/self.IntensityService
        p_0=0
        for n in range(0, ChannelCount+1):
            p_0+=(self.MultIntensity**n)/SMO.factorial(n)
        p_0=p_0**(-1)
        self.ProbabilityService=self.Intensity/(self.Intensity+self.IntensityService)
        self.RelativeBandwidth=self.ProbabilityService
        self.ProbabilityFault=p_0*((self.MultIntensity**ChannelCount)/SMO.factorial(ChannelCount))
        self.Bandwidth=self.Intensity*self.RelativeBandwidth
        self.AverageChannel=self.Bandwidth/self.IntensityService
        
    def MultiChannelWithQueue(self, count,len):
        p=self.Intensity/self.IntensityService
        
        if (p/count)==1:
            p_0=0
            for n in range(0, count+1):
                p_0+=(p**n)/SMO.factorial(n)
            p_0+=(len*(p**(count+1)))/(SMO.factorial(count)*count) 
            p_0=p_0**(-1)
        else:
            p_0=0
            for n in range(0, count+1):
                p_0+=(p**n)/SMO.factorial(n)
            p_0+=(((p**(count+1))/(SMO.factorial(count)*(count-p)))*(1-((p/count)**len)))
            p_0=p_0**(-1)
        self.ProbabilityFault=((p**(count+len))/((count**len)*SMO.factorial(count)))*p_0
       
        if (p/count)==1:
                self.QueueLength=((p*(count+1))/(count*SMO.factorial(count)))*((len*(len+1))/2)*p_0
        else:
             self.QueueLength=((p*(count+1))/(count*SMO.factorial(count)))*((1-(((p/count)**len)*(len+1-(len*p/count))))/((1-(p/count))**2))*p_0
        self.WaitTime=self.QueueLength/self.Intensity
        self.ProbabilityFault=(p**(count+len))*((p_0)/((count**len)*SMO.factorial(count)))
        self.SMOTime=self.WaitTime+((1-self.ProbabilityFault)/(self.IntensityService))
        self.AverageChannel=(self.Intensity/self.IntensityService)*(1-self.ProbabilityFault)
        
    def MultiChannelWithQueueWithoutLen(self, count):
        p=self.Intensity/self.IntensityService
        if (p/count)<1:
            self.IsStatic=True
            p_0=0
            for n in range(0, count+1):
                p_0+=(p**n)/SMO.factorial(n)
            p_0+=(p**(count+1))/(SMO.factorial(count)*(count-p))
            p_0=p_0**(-1)
            self.ProbabilityQueue=((p**(count+1))/((count-p)*SMO.factorial(count)))*p_0
            self.QueueLength=(count/(count-p))*p_0
            self.WaitTime=self.QueueLength/self.Intensity
            self.AverageChannel=p
            self.Lsmo=self.QueueLength+self.AverageChannel
            self.SMOTime=self.WaitTime+1/self.IntensityService
        else:
            self.IsStatic=False
    
    def factorial(n):
        factorial = 1
        while n > 1:
                factorial *= n
                n -= 1
        return factorial

