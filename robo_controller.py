"""naopy controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Keyboard, Motion

timestep = 32

robot = Robot()

keyboard = Keyboard()
keyboard.enable(timestep)


# create the Robot instance.

wave = Motion('../../motions/wave.motion')

while robot.step(timestep) != -1:
    key = keyboard.getKey()
    
    if key == Keyboard.UP:
        wave.play()