
import os, sys
sys.path.append(os.path.join("."))
from siyiA8mini import siyisdk


def main():
    cam = siyisdk.SIYISDK(SERVER_IP="192.168.144.25", SERVER_PORT=37260, BUFF_SIZE=1000)
    print('get_position:', cam.get_position())
    
    
if __name__ == '__main__':
    main()