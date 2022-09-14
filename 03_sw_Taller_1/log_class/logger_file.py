import datetime
import log_class.logger as Logger

path_log_file = 'file.log'

class LoggerFile(Logger.Logger):
    def messageInfo(self, message, object):
        self.__printFile('INFO', message, object)

    def messageWarning(self, message, object):
        self.__printFile('WARNING', message, object)

    def messageError(self, message, object):
        self.__printFile('ERROR', message, object)
    
    def messageDebug(self, message, object):
        self.__printFile('DEBUG', message, object)
    
    def __printFile(self, nivel, message, object):
        with open(path_log_file, 'a') as file:
            data = f'{str(datetime.datetime.now())} [{nivel}] {message, str(object)}\n'
            file.writelines(data)