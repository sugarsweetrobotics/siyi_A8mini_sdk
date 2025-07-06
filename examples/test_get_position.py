
import os, sys
sys.path.append(os.path.join("."))
from siyiA8mini import siyisdk


def main():
    host = "192.168.144.25"
    port = 37260
    bufsize = 1000


    cam = siyisdk.SIYISDK(host, port, bufsize)
    print('get_position:', cam.get_position())
    
    
if __name__ == '__main__':
    main()