from colorama import init, Fore

import datetime
import log_class.logger as Logger

init(autoreset=True)

class LoggerConsole(Logger.Logger):
    
    def messageInfo(self, message, object):
        print(f'{Fore.BLUE}{datetime.datetime.now()} [INFO] {message, object}')
    
    def messageWarning(self, message, object):
        print(f'{Fore.YELLOW}{datetime.datetime.now()} [WARNING] {message, object}')

    def messageError(self, message, object):
       print(f'{Fore.RED}{datetime.datetime.now()} [ERROR] {message, object}')

    def messageDebug(self, message, object):
        print(f'{Fore.MAGENTA}{datetime.datetime.atetime.now()} [DEBUG] {message, object}')
