import log_class.logger_factory_impl as LoggerFactoryImpl

def main() -> None:
    type_logger = str(input("""
        [c]Para salida por consola
        [f]Para salida hacia el archivo
        [e]Para salida por email
        >>>: """))
    logger = LoggerFactoryImpl.LoggerFactoryImpl().get_logger(type=type_logger)
    logger.messageInfo('Mensage generico', 200)
    logger.messageWarning('Mensage generico', 404)
    logger.messageError('Mensage generico', 401)
    logger.messageDebug('Mensage generico', 500)

if __name__ == '__main__':
    main()