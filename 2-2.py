#2-2from mcpi.minecraft import Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
mc.setBlock(x,y,z+2,169)
mc.setBlock(x,y,z-2,169)
mc.setBlock(x-2,y,z,169)
mc.setBlock(x+2,y,z,169)
mc.setBlock(x+1,y,z+1,169)
mc.setBlock(x-1,y,z+1,169)
mc.setBlock(x+1,y,z-1,169)
mc.setBlock(x-1,y,z-1,169)


