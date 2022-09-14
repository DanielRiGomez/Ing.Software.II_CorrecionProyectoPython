import log_class.logger as Logger
import log_class.connector_mail as LogMail

receiver_email_address = 'destino@uptc.edu.co'

class LoggerMail(Logger.Logger): 

    def messageInfo(self, message, object):
       self.__printMail(receiver_email_address, 'INFO', message, object)

    def messageWarning(self, message, object):
       self.__printMail(receiver_email_address,'WARNING', message, object)

    def messageError(self, message, object):
        self.__printMail(receiver_email_address, 'ERROR', message, object)
    
    def messageDebug(self, message, object):
        self.__printMail(receiver_email_address, 'DEBUG', message, object)

    def __printMail(self,receiver_email_address, nivel, message, object):
        mail_log = LogMail.ConnectorMail(receiver_email_address, nivel, message, object)
        mail_log.send_email()