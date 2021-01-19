#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32
import curses

role_name = 'vehicle_cpsc335_name'

#---------
#YOUR CODE (Publishers)
#---------

def keyboard_control():
	stdscr = curses.initscr()
	curses.noecho()
	curses.cbreak()
	stdscr.keypad(1)

	throttle = 0
	steer = 0

	key = ''
	while key != ord('q'):	#loop until pressing `q`
		stdscr.clear()

		stdscr.addstr(0, 5, "Throttle: %lf" % throttle)
		stdscr.addstr(1, 5, "Steering: %lf" % steer)		
		stdscr.addstr(2, 5, "----------------")
		stdscr.addstr(3, 5, "Spacbar: reset")		
		stdscr.addstr(4, 5, "q: quit")

		key = stdscr.getch()

		#NOTE: throttle and steer increase/decrease by 0.05 when key_up/down/left/right is pressed
		
		if key == curses.KEY_UP:
			#---------
			#YOUR CODE
			#---------
		elif key == curses.KEY_DOWN:
			#---------
			#YOUR CODE
			#---------
		elif key == curses.KEY_LEFT:
			#---------
			#YOUR CODE
			#---------
		elif key == curses.KEY_RIGHT:
			#---------
			#YOUR CODE
			#---------
		elif key == ord(' '): #Spacebar: reset throttle and steer to zero
			#---------
			#YOUR CODE
			#---------

		#---------
		#YOUR CODE (publish messages)
		#---------

	curses.nocbreak()
	stdscr.keypad(0)
	curses.echo()
	curses.endwin()

if __name__ == '__main__':
	rospy.init_node('keyboard_control_{}'.format(role_name), anonymous=False)	
	try:
		keyboard_control()
	except rospy.ROSInterruptException:
	        pass
