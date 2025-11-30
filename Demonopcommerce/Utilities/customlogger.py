import logging
import os

class LogGen:

    @staticmethod
    def loggen():
        log_dir = os.path.join(os.getcwd(), "Logs")
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        logging.basicConfig(
            filename=os.path.join(log_dir, "automation.log"),
            format='%(asctime)s: %(levelname)s: %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p'
        )

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
