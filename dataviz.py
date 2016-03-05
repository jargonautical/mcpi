# import minecraft libraries
import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()

# get player position
pPos = mc.player.getTilePos()
print pPos

# post a message to chat
mc.postToChat("Have some data ... ")
mc.postToChat(data)

# set the data array
data = (1,3,2,4)
# clear a space and create a baseplate
mc.setBlocks(pPos.x-5,pPos.y+20,pPos.z-5,pPos.x+5,pPos.y,pPos.z+10,block.AIR)
mc.setBlocks(pPos.x-5,pPos.y,pPos.z-5,pPos.x+5,pPos.y,pPos.z+10,block.SNOW_BLOCK)

# add blocks for data
mc.setBlocks(pPos.x+1,pPos.y,pPos.z+1,pPos.x+1,pPos.y+data[0],pPos.z+1,block.DIAMOND_BLOCK)
mc.setBlocks(pPos.x+1,pPos.y,pPos.z+2,pPos.x+1,pPos.y+data[1],pPos.z+2,block.GOLD_BLOCK)
mc.setBlocks(pPos.x+1,pPos.y,pPos.z+3,pPos.x+1,pPos.y+data[2],pPos.z+3,block.IRON_BLOCK)
mc.setBlocks(pPos.x+1,pPos.y,pPos.z+4,pPos.x+1,pPos.y+data[3],pPos.z+4,block.LAPIS_LAZULI_BLOCK)
