# Bouncing balls example using pi3d module
# ========================================
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
# Bouncing demonstrates pi3d sprites over the desktop.
# It uses the orthographic view scaled to the size of the window;
# this means that sprites can be drawn at pixel resolution
# which is more common for 2D.  Also demonstrates a mock title bar.

import pi3d, sys, random, array

# Setup display and initialise pi3d
scnx=1280
scny=1024
display = pi3d.display()
display.create2D(0,0,scnx,scny,0)

# Set last value (alpha) to zero for a transparent background!
display.setBackColour(0,0.2,0.6,0.8)    	
    
# Ball parameters

arialFont = pi3d.font("MicrosoftSansSerif","#ffffff")   #load AR_CENA font and set the font colour to 'raspberry'

bar = pi3d.loadTexture("textures/bar.png")
bbtitle = pi3d.loadTextureAlpha("textures/pi3dbbd.png",True)
coffee = pi3d.loadTexture("textures/COFFEE.PNG")

# Fetch key presses
mykeys = pi3d.key()
scshots = 1

while True:
	
    display.clear()
   
    #draw a bar at the top of the screen
    pi3d.rectangle(bar,0,scny,scnx,32)
    pi3d.rectangle(bbtitle,5,scny,256+5,32)
    pi3d.rectangle(coffee,200,600,400,400)
    pi3d.drawString(arialFont, "`Test arial font!", 300, 300, 0, 0.0, 1.0,1.0)

    display.swapBuffers()
