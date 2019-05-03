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

# ###################################################################################
# VERSION SIMPLIFIEE POUR DEMARREE UNIQUEMENT LE CHATBOT
# PERMET DE DEVELOPPER LE CHAT SANS AVOIR A TOUT REDEMARRER A CHAQUE FOIS
# ###################################################################################


##############
# Main inmoov service
#i01 = Runtime.createAndStart("i01", "InMoov")


##############
# robot checkup and initialisation ( skeleton & services )
RuningFolder="InMoov"

# libraries import
execfile(RuningFolder+'/system/Import_Libraries.py')
# common functions
execfile(RuningFolder+'/system/Import_Functions.py')

RuningFolder=os.getcwd().replace("\\", "/")+"/"+RuningFolder+"/"

LaunchSwingGui = True
execfile(RuningFolder+'services/2_SwingGui.py'.encode('utf8'))

chatBot = Runtime.createAndStart("chatBot", "ProgramAB")
#RuningFolder = "E:\ulco-fcu\inmoov\InMoov\"
isChatbotActivated = True
if isChatbotActivated:
    chatBot.repetition_count(10)
    chatBot.setPath(RuningFolder + "chatbot/")
    chatBot.startSession("default", "fr")
    # talkEvent(lang_chatbotActivated)
    # chatBot.addTextListener(htmlFilter)
    # htmlFilter.addListener("publishText", python.name, "talk")
    chatBot.setPredicate("default", "topic", "default")
    chatBot.setPredicate("default", "questionfirstinit", "")
    chatBot.setPredicate("default", "tmpname", "")
    chatBot.setPredicate("default", "null", "")
    # chatBot.setPredicate("default","MagicCommandToWakeUp",MagicCommandToWakeUp)
    if chatBot.getPredicate("default", "name") != "" and (
            chatBot.getPredicate("default", "lastUsername") == "" or chatBot.getPredicate("default",
                                                                                          "lastUsername") == "unknown"):
        chatBot.setPredicate("default", "lastUsername", unicode(chatBot.getPredicate("default", "name"), 'utf-8'))
    chatBot.savePredicates()
    # start session based on last recognized person
    if chatBot.getPredicate("default", "lastUsername") != "" and chatBot.getPredicate("default","lastUsername") != "unknown": chatBot.setUsername(unicode(chatBot.getPredicate("default", "lastUsername"), 'utf-8'))
