import os

def clear():
   linux = 'clear'
   windows = 'cls'
   os.system([linux, windows][os.name == 'nt'])