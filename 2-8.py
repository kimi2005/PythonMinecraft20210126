# 2-8
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

answer = int(input('請問你右邊要放什麼方塊:'))
mc.setBlock(x+1,y,z,answer)

userName = input("請輸入姓名:")
message = input("請輸入發言:")
mc.postToChat(" <"+userName+"> " + message)
              