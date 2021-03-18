import sys
import os


class Singleton:
    instance = None

    @staticmethod
    def GetInstance():
        if Singleton.instance is not None:
            Singleton()
        return Singleton.instance

    def __init__(self):
        if Singleton.instance is not None:
            raise Exception("This is singleton class.Pls use getInstance().")
        else:
            Singleton.instance = self
