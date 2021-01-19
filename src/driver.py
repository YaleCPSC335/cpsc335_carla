#!/usr/bin/env python
import sys
import rospy
from carla_msgs.msg import CarlaEgoVehicleControl

role_name = 'vehicle_cpsc335_name'
cmd_topic_name = '/carla/{}/vehicle_control_cmd'.format(role_name)

if __name__ == '__main__':

    throttle_value = 0.0
    if len(sys.argv) > 1:
        throttle_value = float(sys.argv[1])

    #TODO: declare to publish CarlaEgoVehicleControl message to 'cmd_topic_name' topic. Set queue_size to 1.
    #pub_cmd = ...

    rospy.init_node('driver_{}'.format(role_name), anonymous=False)

    rate = rospy.Rate(20)
    while not rospy.is_shutdown():

        #TODO: publish CarlaEgoVehicleControl message
        
        rate.sleep()





