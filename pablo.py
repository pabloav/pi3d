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
import math

# Setup display and initialise pi3d
display = pi3d.display()
display.create3D(1,1,1280,1024)   	# x,y,width,height
display.setBackColour(0,0,0,1)    	# r,g,b,alpha

# Load textures

# Setting 2nd param to True renders 'True' Blending
# (this can be changed later to 'False' with 'cloudimg.blend = False')
myplane = pi3d.createPlane(300, 300, 'box', 100, 100, 0)

starsimg = pi3d.loadTexture("textures/stars2.jpg")

arialFont = pi3d.font("MicrosoftSansSerif","#dd00aa")   #load AR_CENA font and set the font colour to 'raspberry'
destineFont = pi3d.font("Tahoma", "#0055ff")

# Fetch key presses
mykeys = pi3d.key()

rot=0.0

# Display scene
while 1:
    display.clear()

    rot=rot+0.2
    
    pi3d.identity()

#    pi3d.sprite(starsimg, 0,0,-20, 20,20,rot)
#    pi3d.rectangle(starsimg, 0,0,-20, 20,20,rot)

#    myplane.draw(starsimg)
    #                                           x oof, y off, z off, angle, x scale, y scale
    pi3d.drawString(arialFont, "`Test arial font!" ,    math.sin(rot/100), math.cos(rot/100), -2.2, rot, 0.003, 0.003)
#    pi3d.drawString(destineFont, ".Test destine font!", math.cos(rot/100), math.sin(rot/100) - 0.3, -2.2, -rot, 0.001, 0.001)
    
    display.swapBuffers()
