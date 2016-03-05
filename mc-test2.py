# import minecraft libraries
import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()

# get player position
pPos = mc.player.getTilePos()
print pPos

# post a message to chat
mc.postToChat("Hello World!")

# change block
print "Create 3x3 stone cube"
mc.setBlocks(pPos.x-1,pPos.y,pPos.z-1,pPos.x+1,pPos.y+2,pPos.z+1,block.WATER)

print "Position player on top"
mc.player.setPos(pPos.x,pPos.y+3,pPos.z)

mc.postToChat("Move and have another go!")

# mc.player.setPos(23.0,38.0,5.0)
# mc.setBlock(22.0,38.0,6.0,block.DIAMOND_BLOCK)

#get block event hits that have occured since the last time the function was run
blockEvents = mc.events.pollBlockHits()
for blockEvent in blockEvents:
    print blockEvent


