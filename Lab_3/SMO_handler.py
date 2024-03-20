from SMO import *

class SMO_handler:
    
    def __init__(self,serviceTime, intensity, intensityservice=0):
        self.smo = SMO(intensity,serviceTime, intensityservice)
    def SingleChannelWithFail(self):
        self.smo.SingleChannelWithFail()
        return ("Вероятность обслуживания: " + str(self.smo.ProbabilityService) + "\n" + 
                "Вероятность отказа: " + str(self.smo.ProbabilityFault) + "\n" + 
                "Время простоя: " + str(self.smo.DownTime) + "\n"+ 
                "Пропускная способность: " + str(self.smo.Bandwidth) + "\n")

    
        
    def SingleChannelWithQueue(self, queue_length,):
        self.smo.SingleChannelWithQueue(queue_length)
        return ("Вероятность обслуживания: " + str(self.smo.ProbabilityService) + "\n" + 
                "Вероятность отказа: " + str(self.smo.ProbabilityFault) + "\n" + 
                "Абсолютная пропускная способность: " + str(self.smo.RelativeBandwidth) + "\n" +
                "Среднее число занятых каналов: " + str(self.smo.AverageChannel) + "\n" +
                "Средняя длина очереди: " + str(self.smo.QueueLength) + "\n" +
                "Среднее время ожидания в очереди: " + str(self.smo.WaitTime) + "\n"+
                "Среднее число заявок в СМО: " + str(self.smo.Lsmo) + "\n" +
                "Cреднее время нахождения заявки в СМО: " + str(self.smo.SMOTime) + "\n")
    
            
            
    def SingleChannelWithQueueWhithoutLen(self):
        self.smo.SingleChannelWithQueueWhithoutLen()
        if(self.smo.IsStatic):
            return ("Средняя длина очереди: " + str(self.smo.QueueLength) + "\n" +
                    "Среднее время ожидания в очереди: " + str(self.smo.WaitTime) + "\n"+
                    "Среднее число заявок в СМО: " + str(self.smo.Lsmo) + "\n" +
                    "Cреднее время нахождения заявки в СМО: " + str(self.smo.SMOTime) + "\n")
        else:
            return "Стационарное состояние невозможно\n"   
            
            
    def MultiChannelWithFail(self, channel_count):
        self.smo.MultiChannelWithFail(channel_count)
        return ("Вероятность обслуживания: " + str(self.smo.ProbabilityService) + "\n" + 
                "Вероятность отказа: " + str(self.smo.ProbabilityFault) + "\n" + 
                "Относительнаяпропускная способность: " + str(self.smo.RelativeBandwidth) + "\n" +
                "Абсолютная пропускная способность: " + str(self.smo.Bandwidth) + "\n"+
                "Среднее число занятых каналов: " + str(self.smo.AverageChannel) + "\n")
        
            
    def MultiChannelWithQueue(self, channel_count,queue_length):
        
        self.smo.MultiChannelWithQueue(channel_count,queue_length)
        return ("Вероятность отказа: " + str(self.smo.ProbabilityFault) + "\n" + 
                "Среднее число занятых каналов: " + str(self.smo.AverageChannel) + "\n" +
                "Средняя длина очереди: " + str(self.smo.QueueLength) + "\n" +
                "Среднее время ожидания в очереди: " + str(self.smo.WaitTime) + "\n"+
                "Cреднее время нахождения заявки в СМО: " + str(self.smo.SMOTime) + "\n")
        
        
    def MultiChannelWithQueueWithoutLen(self, channel_count):
        self.smo.MultiChannelWithQueueWithoutLen(channel_count)
        if(self.smo.IsStatic):
            return ("Вероятность образования очереди: " + str(self.smo.ProbabilityQueue) + "\n"
                    "Среднее время ожидания в очереди: " + str(self.smo.WaitTime) + "\n"+
                    "Среднее число заявок в СМО: " + str(self.smo.Lsmo) + "\n" +
                    "Cреднее время нахождения заявки в СМО: " + str(self.smo.SMOTime) + "\n"+
                    "Среднее число занятых каналов: " + str(self.smo.AverageChannel) + "\n")
        else: 
            return "Стационарное состояние невозможно\n"

    
    