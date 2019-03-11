##						   ___  ________   _____ ______   ________  ________  ___      ___ 
##						  |\  \|\   ___  \|\   _ \  _   \|\   __  \|\   __  \|\  \    /  /|
##						  \ \  \ \  \\ \  \ \  \\\__\ \  \ \  \|\  \ \  \|\  \ \  \  /  / /
##						   \ \  \ \  \\ \  \ \  \\|__| \  \ \  \\\  \ \  \\\  \ \  \/  / / 
##						    \ \  \ \  \\ \  \ \  \    \ \  \ \  \\\  \ \  \\\  \ \    / /  
##						     \ \__\ \__\\ \__\ \__\    \ \__\ \_______\ \_______\ \__/ /   
##						      \|__|\|__| \|__|\|__|     \|__|\|_______|\|_______|\|__|/    
version='1.0.0'

# this will run with versions of MRL above :
mrlCompatible='2685'
# DEMARRAGE MINIMAL AVEC JUSTE LE SUPPORT JOYSTICK
#
#
# ###################################################################################
# This is the full configurable launcher script for Inmoov service :
# MORE informations here : http://myrobotlab.org/service/InMoov
# At this time configurable things are inside the config folder. 
# By default virtual environment is started, so you can test things with no risk ! 
#
# To start using the Finger Starter with real hardware, set : 
# ( The Finger Starter is considered here to be right index, 
# so make sure your servo is connected to pin3 of you Arduino )
##
#   ScriptType=RightSide | inside config/_InMoov.config
#   MyRightPort=COMx | inside config/_service_6_Arduino.config
#   isRightHandActivated=True | inside config/skeleton_rightHand.config
#   voice command sample : OPEN HAND
##
# Check your configuration inside Inmoov.config
# Change voice and speech engine inside mouth.config
# If you setup 2 arduino + configs in skeleton folder, it can run full Inmoov or separated parts ( right hand / head ... )
# ###################################################################################

SwingGui = Runtime.createAndStart("SwingGui", "SwingGui")
joystick = Runtime.createAndStart("joystick", "Joystick")
