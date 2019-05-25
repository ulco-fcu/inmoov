#Projet NEO

Techniquement :
- repository pour gerer la config / le developpement du projet NEO du Centre de FOrmation Universitaire de l'Universite du Littoral
- TODO : 
- Le DEv de NEO se fera depuis la branche 'dev-manticore'.
- Vous veillerez donc à travailler depuis cette branche 

Dependances : 
MyRobotLab version Manticore 
[A Telecharger ICI](https://github.com/MyRobotLab/myrobotlab/releases/tag/1.0.2693)
Intégré dans la branche dev-manticore


#Tutos :
- myrobotlab + gestes :
1. https://inmoov.monsite-orange.fr/page-5c5c0b5c22b9a.html
 
- git : 
1. https://git-scm.com/book/fr/v2
2. http://rogerdudler.github.io/git-guide/index.fr.html

- chatbot (programAB) : 
1. https://code.google.com/archive/p/program-ab/wikis
2. https://www.tutorialspoint.com/aiml/index.htm


--------------

# InMooV - Service launcher v 1.0.0   

This is the full configurable internationnal launcher script for Inmoov service.  
Worky out of the box with standardized InMoov hardware configuration.  


![virtual inmoov screenshot](http://www.myai.cloud/pic/main.png)

## Getting Started
MORE informations here : http://myrobotlab.org/service/InMoov  
  
At this time ( v 1.0.0 ) , configurable things are inside the config folder.   
By default virtual environment is started, so you can test things with no risk !  

![virtual inmoov screenshot](http://www.myai.cloud/pic/virtual.png)
  
To start using the Finger Starter with real hardware, set :  
 ( The Finger Starter is considered here to be right index, so make sure your servo is connected to pin3 of you Arduino )  

```
ScriptType=RightSide | inside config/_InMoov.config  
MyRightPort=COMx | inside config/_service_6_Arduino.config  
isRightHandActivated=True | inside config/skeleton_rightHand.config  
voice command sample : OPEN HAND  
```

Check your configuration inside Inmoov.config ( exemple to change english to french )  
If you setup 2 arduino + configs in skeleton folder, it can run full Inmoov or separated parts ( right hand / head ... )  

  
### DOCUMENTATION & HELP  
http://myrobotlab.org/service/InMoov  
  
bugs report : https://github.com/MyRobotLab/inmoov/issues  

### CONTRIBUTION  
Is welcome :)  
( On the develop branch )  
  
### CHANGELOG  
   
0.9.9  
/ Testing...  
0.7.0  
/ Chatbots enhancements & fixes...  
0.6.1  
/ add AndroidSpeechRecognizer   