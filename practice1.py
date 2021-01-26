# practice1
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random

while True:
    x,y,z = mc.player.getTilePos()
    
    color = random.randrange(0,16)
    
    mc.setBlock(x,y,z,38,color)