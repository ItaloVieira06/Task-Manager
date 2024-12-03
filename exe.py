import subprocess
from interface.main_window import *

#executável
if __name__ == '__main__':
     cmd = "main.py -u abcd -p 1234"
     subprocess.call(cmd, Shell=True)