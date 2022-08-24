from ast import Str
import datetime as dt
from pydoc import doc
import tkinter as tk

def getTimeStyles(timeInput: dt.datetime,isInternationalTime:bool):
    pass


def datetimeToString(timeInput: dt.datetime, isInternationalTime:bool) -> Str:
    return timeInput.strftime("%m-%d-%y at %H:%M:%S ")
    #return str(timeInput.strftime("%m")+"-"+timeInput.strftime("%d")+"-"+timeInput.strftime("%y")+" at "+timeInput.strftime("%I")+":"+timeInput.strftime("%M")+" "+timeInput.strftime("%p")+" in " )

class userData:
    def __init__(self, name) -> None:
        self.name = name
        self.

class message:
    def __init__(self, user: userData, time:dt.datetime, sent:str):
        """_summary_

        Args:
            user (userData): _description_
            time (dt.datetime): _description_
            sent (str): _description_
        """
        self.user = user;

        self.time = time

        self.sent = sent

    
    def readMessage(self) -> str:
        readFinal = self.user + " > " + datetimeToString(self.time,True) + ": " + self.sent
        return readFinal



uin = message("Isaac",dt.datetime.now(),"Test")
print(dt.datetime.now().strftime("%z"))
print(uin.readMessage())

