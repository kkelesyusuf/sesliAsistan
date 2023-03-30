import types
from Core.SpeechGenerator import SpeechGenerator
from Skills.Calendar import Calendar
from Skills.Traffic import Traffic

class Brain:
    def __init__(self):
        self.speak=SpeechGenerator().say

    def __check(self,input,keywords):
        return bool(any(key in input for key in keywords))

    def __try_to(self,get_result,for_context):
        if isinstance(get_result,types.FunctionType):
            res=get_result()
        else:
            res=get_result

        if not res or isinstance(res,Exception):
            self.speak(f"{for_context} bilgisine ulaşılamadı.")
        else:
            self.speak(res)
    def make_sense(self, input, time_keywords=None):
        if not input:
            return

        i=input.casefold()
        if self.__check(i,Calendar.time_keywords):
            self.speak(Calendar().get_time())

        elif self.__check(i,Calendar.date_keywords):
            self.speak(Calendar().get_date()[0])

        elif self.__check(i,Traffic.keywords):
            self.__try_to(Traffic().get_traffic_density(),"Trafik Yoğunluğu")


        else:
            self.speak("Ne söylediğinizi anlayamadım.")
