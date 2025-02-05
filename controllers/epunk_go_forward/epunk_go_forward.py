"""epunk_go_forward controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor
TIME_STEP = 64
max_speed = 3.89

# create the Robot instance.
robot = Robot()

leftMotor = robot.getDevice('left wheel motor')
rightMotor = robot.getDevice('right wheel motor')
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
# rightMotor.setPosition(10.0)
leftMotor.setVelocity(0.1*max_speed)
rightMotor.setVelocity(0.1*max_speed)
while robot.step(TIME_STEP) != 0:
    pass
