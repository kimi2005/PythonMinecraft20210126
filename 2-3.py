# 2-3
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random,time
while True:
    x,y,z = mc.player.getTilePos()
    
    color = random.randrange(0,16)
    mc.setBlocks(x+10,y,z+10,x-10,y,z-10,46,color)
    import random,time
    time.sleep(0)