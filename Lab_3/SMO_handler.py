from SMO import *


class SMO_handler:

    def __init__(self, serviceTime, intensity, intensityservice=0):
        self.smo = SMO(intensity, serviceTime, intensityservice)

    def SingleChannelWithFail(self):
        self.smo.SingleChannelWithFail()
        return ("Вероятность обслуживания: " + "{:2f}".format(self.smo.ProbabilityService) + "\n" +
                "Вероятность отказа: " + "{:2f}".format(self.smo.ProbabilityFault) + "\n" +
                "Время простоя: " + "{:2f}".format(self.smo.DownTime) + "\n" +
                "Пропускная способность: " + "{:2f}".format(self.smo.Bandwidth) + "\n")

    def SingleChannelWithQueue(self, queue_length,):
        self.smo.SingleChannelWithQueue(queue_length)
        return ("Вероятность обслуживания: " + "{:2f}".format(self.smo.ProbabilityService) + "\n" +
                "Вероятность отказа: " + "{:2f}".format(self.smo.ProbabilityFault) + "\n" +
                "Абсолютная пропускная способность: " + "{:2f}".format(self.smo.RelativeBandwidth) + "\n" +
                "Среднее число занятых каналов: " + "{:2f}".format(self.smo.AverageChannel) + "\n" +
                "Средняя длина очереди: " + "{:2f}".format(self.smo.QueueLength) + "\n" +
                "Среднее время ожидания в очереди: " + "{:2f}".format(self.smo.WaitTime) + "\n" +
                "Среднее число заявок в СМО: " + "{:2f}".format(self.smo.Lsmo) + "\n" +
                "Cреднее время нахождения заявки в СМО: " + "{:2f}".format(self.smo.SMOTime) + "\n")

    def SingleChannelWithQueueWhithoutLen(self):
        self.smo.SingleChannelWithQueueWhithoutLen()
        if (self.smo.IsStatic):
            return ("Средняя длина очереди: " + "{:2f}".format(self.smo.QueueLength) + "\n" +
                    "Среднее время ожидания в очереди: " + "{:2f}".format(self.smo.WaitTime) + "\n" +
                    "Среднее число заявок в СМО: " + "{:2f}".format(self.smo.Lsmo) + "\n" +
                    "Cреднее время нахождения заявки в СМО: " + "{:2f}".format(self.smo.SMOTime) + "\n")
        else:
            return "Стационарное состояние невозможно\n"

    def MultiChannelWithFail(self, channel_count):
        self.smo.MultiChannelWithFail(channel_count)
        return ("Вероятность обслуживания: " + "{:2f}".format(self.smo.ProbabilityService) + "\n" +
                "Вероятность отказа: " + "{:2f}".format(self.smo.ProbabilityFault) + "\n" +
                "Относительнаяпропускная способность: " + "{:2f}".format(self.smo.RelativeBandwidth) + "\n" +
                "Абсолютная пропускная способность: " + "{:2f}".format(self.smo.Bandwidth) + "\n" +
                "Среднее число занятых каналов: " + "{:2f}".format(self.smo.AverageChannel) + "\n")

    def MultiChannelWithQueue(self, channel_count, queue_length):

        self.smo.MultiChannelWithQueue(channel_count, queue_length)
        return ("Вероятность отказа: " + "{:2f}".format(self.smo.ProbabilityFault) + "\n" +
                "Среднее число занятых каналов: " + "{:2f}".format(self.smo.AverageChannel) + "\n" +
                "Средняя длина очереди: " + "{:2f}".format(self.smo.QueueLength) + "\n" +
                "Среднее время ожидания в очереди: " + "{:2f}".format(self.smo.WaitTime) + "\n" +
                "Cреднее время нахождения заявки в СМО: " + "{:2f}".format(self.smo.SMOTime) + "\n")

    def MultiChannelWithQueueWithoutLen(self, channel_count):
        self.smo.MultiChannelWithQueueWithoutLen(channel_count)
        if (self.smo.IsStatic):
            return ("Вероятность образования очереди: " + str(self.smo.ProbabilityQueue) + "\n"
                    "Среднее время ожидания в очереди: " + "{:2f}".format(self.smo.WaitTime) + "\n" +
                    "Среднее число заявок в СМО: " + "{:2f}".format(self.smo.Lsmo) + "\n" +
                    "Cреднее время нахождения заявки в СМО: " + "{:2f}".format(self.smo.SMOTime) + "\n" +
                    "Среднее число занятых каналов: " + "{:2f}".format(self.smo.AverageChannel) + "\n")
        else:
            return "Стационарное состояние невозможно\n"
