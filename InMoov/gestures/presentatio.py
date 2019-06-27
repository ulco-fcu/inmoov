# -- coding: utf-8 --

def presentatio():
  relax()
  i01.startedGesture()
  sleep(1)
  i01.moveHead(80,86)
  i01.moveArm("left",53,0,60,10)
  i01.moveArm("right",42,50,60,18)
  sleep(2)
  i01.moveHead(80,86)
  i01.moveArm("left",53,50,60,10)
  i01.moveArm("right",42,0,60,18)
  sleep(2)
  i01.moveHead(80,86)
  i01.moveArm("left",53,0,60,10)
  i01.moveArm("right",42,100,60,18)
  sleep(2)
  i01.moveHead(80,86)
  i01.moveArm("left",53,100,60,10)
  i01.moveArm("right",42,0,60,18)
  sleep(2)
  i01.finishedGesture()
  relax()



