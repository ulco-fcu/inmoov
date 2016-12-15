#TODO:
#set here the minimum config so that InMoov can work
#a finger starter or a full inmoov should be able to work with this
#min and max?
#mappings?

# ##############################################################################
# 							BASIC CONFIGURATION
# ##############################################################################


ScriptType="FingerStarter" 
# FingerStarter: connect one arduino and play with servo
# NoArduino: Chatbot Only
# Full: Inmoov is Alive !

#to tweak the default voice
#Voice="cmu-bdl" #Male US voice.You need to add the necessary file.jar to myrobotlab.1.0.XXXX/library/jar
#https://github.com/MyRobotLab/pyrobotlab/blob/ff6e2cef4d0642e47ee15e353ef934ac6701e713/home/hairygael/voice-cmu-bdl-5.2.jar

# ##############################################################################
# 							LIST OF VOICES AND LANGUAGES
#	MaryTTS : http://myrobotlab.org/content/marytts-multi-language-support
# ##############################################################################

voiceType="cmu-slt-hsmm"
MyLanguage="en"
MyRightPort="COM7" # Your Arduino ComPort : UPLOAD MRLCOMM INSIDE \resource\Arduino\MRLComm\MRLComm.ino !!!












#go for the launch!
execfile('Config/ExtraConfig/InitCheckup.py')