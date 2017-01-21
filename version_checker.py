import cv2
import dronekit
import pymavlink
import rospy
import platform

print "============ VERSION CHECKER ============"
print " Python:     " + platform.python_version()
print " Dronekit:   "
print " MAVLink:    "
print " ROS:        "
print " OpenCV:     " + cv2.__version__
print dronekit.Vehicle.version
print pymavlink.__version__
print rospy.__version__
