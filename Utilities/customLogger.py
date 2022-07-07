import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                            force=True, handlers=[logging.FileHandler(".\\Logs\\automation.log",mode='w'), logging.StreamHandler()])
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

