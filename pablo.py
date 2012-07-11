# Earth and example shapes using pi3d module
# ==========================================
# Copyright (c) 2012 - Tim Skillman
# Version 0.02 - 03Jul12
# 
# This example does not reflect the finished pi3d module in any way whatsoever!
# It merely aims to demonstrate a working concept in simplfying 3D programming on the Pi
#
# PLEASE INSTALL PIL imaging with:
#
#      $ sudo apt-get install python-imaging
#
# before running this example
#

import pi3d

# Setup display and initialise pi3d
display = pi3d.display()
display.create3D(1,1,1280,1024)   	# x,y,width,height
display.setBackColour(0,0,0,1)    	# r,g,b,alpha

# Load textures

# Setting 2nd param to True renders 'True' Blending
# (this can be changed later to 'False' with 'cloudimg.blend = False')

arialFont = pi3d.font("AR_CENA","#dd00aa")   #load AR_CENA font and set the font colour to 'raspberry'
destineFont = pi3d.font("AR_DELANEY", "#0055ff")

# Fetch key presses
mykeys = pi3d.key()

rot=0.0

# Display scene
while 1:
    display.clear()

    rot=rot+0.2
    
    pi3d.identity()

    pi3d.drawString(arialFont, "Test arial font!" ,    -1.0,  0.0, -2.2, rot, 0.003, 0.003)
    pi3d.drawString(destineFont, "Test destine font!", -1.0, -0.3, -2.2, rot, 0.002,0.002)
    
    display.swapBuffers()
