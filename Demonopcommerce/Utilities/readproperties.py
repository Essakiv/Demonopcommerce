import configparser
import os


class Readconfig:

    @staticmethod
    def _load_config():
        config = configparser.RawConfigParser()

        # Build absolute path to the config file
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        config_path = os.path.join(base_dir, "Configurations", "config.ini")

        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Config file not found: {config_path}")

        config.read(config_path)
        return config

    @staticmethod
    def getApplicationURL():
        config = Readconfig._load_config()
        return config.get('common.info', 'baseurl')

    @staticmethod
    def getUseremail():
        config = Readconfig._load_config()
        return config.get('common.info', 'useremail')

    @staticmethod
    def getPassword():
        config = Readconfig._load_config()
        return config.get('common.info', 'password')
