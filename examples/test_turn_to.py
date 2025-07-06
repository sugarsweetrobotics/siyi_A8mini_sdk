
import os, sys, time
sys.path.append(os.path.join("."))
from siyiA8mini import siyisdk


def main():
    cam = siyisdk.SIYISDK(SERVER_IP="192.168.144.25", SERVER_PORT=37260, BUFF_SIZE=1000)
    
    # print('turn_to: yaw=0.0, pitch=0.0')
    cam.turn_to(yaw=10.0, pitch=-20.0)
    time.sleep(1.0) 
    
    print(cam.get_position())
    
    # print('turn_to: yaw=90.0, pitch=0.0')
    # cam.turn_to(yaw=90.0, pitch=0.0)
    # time.sleep(1.0)    
    
    # print('turn_to: yaw=-90.0, pitch=0.0')
    # cam.turn_to(yaw=-90.0, pitch=0.0)
    # time.sleep(2.0)    
    
    # print('turn_to: yaw=0.0, pitch=0.0')
    # cam.turn_to(yaw=0.0, pitch=0.0)
    # time.sleep(1.0)   
    
    # print('turn_to: yaw=0.0, pitch=20.0')
    # cam.turn_to(yaw=0.0, pitch=20.0)
    # time.sleep(1.0)   
    
    # print('turn_to: yaw=0.0, pitch=-30.0')
    # cam.turn_to(yaw=0.0, pitch=-30.0)
    # time.sleep(2.0)  
    
    # print('turn_to: yaw=0.0, pitch=0.0')
    # cam.turn_to(yaw=0.0, pitch=0.0)
    # time.sleep(1.0)  

    print('exit')
    
if __name__ == '__main__':
    main()