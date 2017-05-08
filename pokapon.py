import pygame
from pygame.locals import *
import time
from datetime import datetime
import random
import pigpio
 
def main() :
    pygame.init()
    pi = pigpio.pi()
    first_time = False
    is_start = False
    is_attacked = False
    is_defenced = False

    #time_threshold = random.uniform(3, 10) # too difficult
    time_threshold = 5

    # Initialized servo position
    pi.set_servo_pulsewidth(12, 500)
    pi.set_servo_pulsewidth(18, 1500)

    while True:
 
        eventlist = pygame.event.get()
 
        eventlist = filter(lambda e : e.type == pygame.locals.JOYBUTTONDOWN , eventlist)

        input_list = map(lambda x : x.button,eventlist)

        # Push A Button is Start.
        if 0 in input_list:
            print 'start'
            first_time = datetime.now()
            is_start = True
 
        if is_start == False:
            continue

        delta = datetime.now() - first_time
        print 'DIFF: ' + str(delta.total_seconds())

        if delta.total_seconds() > time_threshold:
            print 'ATTACK!!!'
            pi.set_servo_pulsewidth(12, 2000)

        # Push ZR Botton is Guard.
        if 15 in input_list:
            print 'DEFENCE!!!'
            pi.set_servo_pulsewidth(18, 500)
 
        # Push B Button is Finish.
        if 2 in input_list:
            print 'FINISH!!'
            pi.set_servo_pulsewidth(12, 500)
            pi.set_servo_pulsewidth(18, 500)
            break

        time.sleep(0.1)
 
if __name__ == '__main__':
    pygame.joystick.init()
    try:
        print 'count: ' + str(pygame.joystick.get_count())
        joys = pygame.joystick.Joystick(0)
        joys.init()
        main()
    except pygame.error:
        print 'error has occured'
