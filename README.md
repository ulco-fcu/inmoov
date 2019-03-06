#Projet NEO
NEO c'est Nous.
 (photo groupe)
 
NEO c'est Lui.
(photo bras + photo complet)

blablablab.. vient de gael ... histo ...

NEO, c'est l'idée, qu'avec un peu de folie et bcp d'acharnement, on est tous capable de transformer le présent en avenir.

NEO, c'est ce support pédagogique, qui va permetre a tous d'apprendre des connaissances de chacun.

NEO, c'est l'intelligence de savoir s'unir pour relever les défis

L'intelligence n'est qu"un artifice, ...blablablab...


-------
Ce projet vise a donner naissance à NEO

Et c'est d'ici qu'il naitra, somme de tous nos efforts.

Il sera la concrétisation de nos ( / des  etudiants) apprentissages en IA
 
-------
Techniquement :
- repository pour gerer la config / le developpement du projet NEO du Centre de FOrmation Universitaire de l'Universite du Littoral
- TODO : 
- Le DEv de NEO se fera depuis la branche 'dev-manticore'.
- Vous veillerez donc à travailler depuis cette branche 


-----
Merci Gael Langevin,
 Ta famille s'agrandit de jour en jour
 
------



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