import os
from modules.conf import Conf
from modules.system_info import SystemInfo

def main():
    config = Conf()
    sys_info = SystemInfo()
    print(sys_info.cpu_cores.enabled_cores)
    return

main()