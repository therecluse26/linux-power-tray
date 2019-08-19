import os
import json

class Conf:
    home_path = "~/"
    config_path = ".config/power-tray/"
    config_file = "config.json"
    config_data = []

    def __init__(self):

        self.home_path = os.path.expanduser(self.home_path)

        full_config_path = self.home_path + self.config_path 
        full_config_file_path = full_config_path + self.config_file

        if os.path.exists(full_config_path):
            if os.path.exists(full_config_file_path):
                # If file exists
                f = open(full_config_file_path)
                self.config_data = f.read()
                f.close()
            else:
                # If directory exists, but no file
                self.__make_new_config(full_config_file_path)
                
        else:
            # If no directory exists
            os.mkdir(full_config_path)
            self.__make_new_config(full_config_file_path)
        return

    def __make_new_config(self, path):
        f = open(path, "w+")
        f.write("[]")
        f.close()
        return