from ast import Str
import datetime as dt
from pydoc import doc
import tkinter

def getTimeStyles(timeInput: dt.datetime,isInternationalTime:bool):
    pass


def datetimeToString(timeInput: dt.datetime, isInternationalTime:bool) -> Str:
    return timeInput.strftime("%m-%d-%y at %H:%M:%S ")
    #return str(timeInput.strftime("%m")+"-"+timeInput.strftime("%d")+"-"+timeInput.strftime("%y")+" at "+timeInput.strftime("%I")+":"+timeInput.strftime("%M")+" "+timeInput.strftime("%p")+" in " )

class message:
    def __init__(self, user, time:dt.datetime, sent:str):
        """_summary_

        Args:
            user (str): _description_
            time (dt.datetime): The time the message is sent
            sent (str): _description_
        """
        self.user = user;

        self.user = str (self.user)

        self.time = time

        self.time = self.time

        self.sent = sent

        self.sent = str (self.sent)


    
    def readMessage(self):
        readFinal = self.user + " > " + datetimeToString(self.time,True) + ": " + self.sent
        return readFinal

uin = message("Isaac",dt.datetime.now(),"Test")
print(dt.datetime.now().strftime("%z"))
print(uin.readMessage())

