# -- coding: utf-8 --

def presentation():
  relax()
  i01.startedGest
  sleep(1)
  i01.moveArm("left",53,0,60,10)
  sleep(2)
  i01.moveArm("left",53,50,60,10)
  sleep(2)
  i01.moveArm("left",53,0,60,10)
  sleep(2)
  i01.moveArm("left",53,100,60,10)
  sleep(0.2)
  i01.finishedGesture()
  relax()



