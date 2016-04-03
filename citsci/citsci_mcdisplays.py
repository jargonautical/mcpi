from mcpi.minecraft import Minecraft
from mcpi import block
from citsci_mcsensors import DisplayTube
from time import sleep, time
from mcclock import Clock

"""
SpaceCRAFT - Astro Pi competition[http://astro-pi.org/] entry
Conceived by Hannah Belshaw
Created by Martin O'Hanlon[http://www.stuffaboutcode.com]
For the Raspberry Pi Foundation[https://www.raspberrypi.org]

mcdisplays.py

Displays information from the Astro Pi in Minecraft
"""

def roundDegrees(number):
    ROUNDDEGREESTO = 15
    return round((number / ROUNDDEGREESTO),0) * ROUNDDEGREESTO

class ISSTowerMinecraftDisplay():
    """
    Visualisation of data in Minecraft - glass tubes or bar charts,
    and a clock showing the time of measurements
    """
    def __init__(self, mc, pos):

        self.mc = mc
        self.pos = pos

        self.time = None
        self.cputemperature = None
        self.temperature = None
        self.humidity = None
        self.pressure = None
        
        #calculate the positions of the towers, iss, clock and stairs
        temppos = pos.clone()
        temppos.x += 3

        humiditypos = pos.clone()
        humiditypos.x += 7

        pressurepos = pos.clone()
        pressurepos.x += 11

        cputemppos = pos.clone()
        cputemppos.x += 15

        clockpos = pos.clone()
        clockpos.x -= 1
        clockpos.z -= 1
        clockpos.y += 35

        #create the clock
        self.clock = Clock(mc, clockpos, block.WOOL.id, 12)

        #clear an area for the tubes
        self.mc.setBlocks(
            self.pos.x - 50,
            self.pos.y,
            self.pos.z - 10,
            self.pos.x + 50,
            self.pos.y + 50,
            self.pos.z + 10,
            block.AIR.id)

        #set a baseplate
        self.mc.setBlocks(
            self.pos.x - 10,
            self.pos.y-1,
            self.pos.z -5,
            self.pos.x + 40,
            self.pos.y-1,
            self.pos.z + 10,
            block.SNOW_BLOCK.id)

        #set a backdrop
        self.mc.setBlocks(
            self.pos.x - 10,
            self.pos.y - 3,
            self.pos.z - 5,
            self.pos.x + 40,
            self.pos.y + 60,
            self.pos.z - 5,
            block.SNOW_BLOCK.id)
        
        #create the tubes
        self.tempTube = DisplayTube(
            mc, temppos, 20,
            10, 40,
            block.WOOL.id, 1)

        self.humidityTube = DisplayTube(
            mc, humiditypos, 20,
            20, 50,
            block.WOOL.id, 2)

        self.pressureTube = DisplayTube(
            mc, pressurepos, 20,
            950, 1050,
            block.WOOL.id, 3)

        self.cputempTube = DisplayTube(
            mc, cputemppos, 20,
            30, 50,
            block.WOOL.id, 4)

    def update(self, time, cpuTemperature, temperature, humidity, pressure, orientation, joystick):        
        #update the clock
        self.clock.setTime(time)

        #update the towers
        self.cputempTube.setValue(cpuTemperature)
        self.tempTube.setValue(temperature)
        self.humidityTube.setValue(humidity)
        self.pressureTube.setValue(pressure)
                    
        #update the values
        self.time = time
        self.cpuTemperature = cpuTemperature
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.orientation = orientation
        self.joystick = joystick

    def clear(self):
        #clear the display
        self.tempTube.clear()
        self.humidityTube.clear()
        self.pressureTube.clear()
        self.cputempTube.clear()
        self.clock.clear()

    
#test
if __name__ == "__main__":
    mc = Minecraft.create()
    pos = mc.player.getTilePos()
    pos.x += 5
    pos.y = mc.getHeight(pos.x, pos.y)
    mcdisplay = ISSTowerMinecraftDisplay(mc, pos)
    try:
        mcdisplay.update(
            time(), 40, 30, 40, 1000,
            {"yaw": 0, "pitch": 0, "roll": 0},
            {"up": 0, "down": 0, "left": 0, "right": 0, "button": 0})
        sleep(10)
        mcdisplay.update(
            time(), 45, 20, 30, 1050,
            {"yaw": 45, "pitch": 45, "roll": 0},
            {"up": 1, "down": 1, "left": 1, "right": 1, "button": 1})
        sleep(10)
    finally:
        mcdisplay.clear()

    
