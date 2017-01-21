# Version checker for Invictus
# Checks for Python, Dronekit, PyMavLink, ROSpy and OpenCV

import cv2
import dronekit
import pymavlink
import rospy
import platform
import subprocess
import re

version_list = []

version_string = subprocess.check_output(["pip", "show", "dronekit", "pymavlink", "rospy"])
pattern = re.compile(r"Version: (\d.*)")
for line in version_string.splitlines():
	temp = pattern.match(line)
	if temp != None:
		temp = pattern.match(line).group(1)
		version_list.append(temp)

print "============ VERSION CHECKER ============"
print "              Python: " + platform.python_version()
print "            Dronekit: " + version_list[0]
print "           pymavlink: " + version_list[1]
print "               rospy: " + version_list[2]
print "              OpenCV: " + cv2.__version__
