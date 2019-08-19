import platform
import multiprocessing
import os

class CpuInfo: 
    architecture = None
    max_frequency = None
    available_cores = None
    enabled_cores = None

    def __init__(self):
        self.get_cpu_arch()
        self.get_cpu_cores()

    def get_cpu_arch(self):
        self.architecture = platform.architecture
    
    def get_cpu_cores(self):
        self.enabled_cores = multiprocessing.cpu_count()
        # self.available_cores = multiprocessing.

    def get_max_frequency(self):
        return
    

class Kernel:
    version = None
    loaded_modules = None
    available_modules = None

    def __init__(self):
        return

    def get_loaded_modules(self):
        return
    
    def get_version(self):
        return

class SystemInfo:
        
    cpu = CpuInfo()
    kernel = Kernel()

    graphics_settings = []
    cpu_arch = ""
    power_governor = ""
    bluetooth_settings = []

    def __init__(self):
        # self.get_cpu_cores()
        self.graphics_settings = self.get_graphic_settings()
        self.power_governor = self.get_power_governor()
        self.bluetooth_settings = self.get_bluetooth_settings()    
    
    def get_graphic_settings(self):
        return []

    def get_power_governor(self):
        return ""

    def get_bluetooth_settings(self):
        return []
