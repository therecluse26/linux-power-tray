import platform
import multiprocessing
import os

class CoreData: 
    available_cores = None
    enabled_cores = None

class SystemInfo:
        
    cpu_cores = CoreData()

    graphics_settings = []
    cpu_arch = ""
    power_governor = ""
    bluetooth_settings = []

    def __init__(self):
        self.get_cpu_cores()
        self.graphics_settings = self.get_graphic_settings()
        self.cpu_arch = self.get_cpu_arch()
        self.power_governor = self.get_power_governor()
        self.bluetooth_settings = self.get_bluetooth_settings()
    
    def get_cpu_cores(self):
        self.cpu_cores.enabled_cores = multiprocessing.cpu_count()
        self.cpu_cores.available_cores = multiprocessing.
        return
    
    def get_graphic_settings(self):
        return []

    def get_cpu_arch(self):
        return platform.architecture
    
    def get_power_governor(self):
        return ""

    def get_bluetooth_settings(self):
        return []
