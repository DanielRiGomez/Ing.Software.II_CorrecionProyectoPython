from abc import ABC, abstractmethod

class Logger(ABC):

    @abstractmethod
    def messageInfo(self, message, object): pass

    @abstractmethod
    def messageWarning(self, message, object): pass

    @abstractmethod
    def messageError(self, message, object): pass

    @abstractmethod
    def messageDebug(self, message, object): pass
