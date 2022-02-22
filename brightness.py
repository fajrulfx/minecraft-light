# Created by Fajrul from Minecraft Science Kingdom
# https://sciencekingdom.gg/vote

from mcpi.minecraft import Minecraft
from yeelight import Bulb
import time
from math import floor

bulb = Bulb("XX.XX.XX.XXX")
mc = Minecraft.create(address="XX.XX.XX.XX", port=25565)

GREEN = False
RED = False
BLUE = False
YELLOW = False

while True:
	pos = mc.player.getPos()
	blockType = mc.getBlock(pos.x, pos.y-1, pos.z)

	if blockType == 2: #grass
		if GREEN == False:
			bulb.set_rgb(0, 255, 0)
			mc.postToChat("  Lampu berubah jadi hijau!")
			GREEN = True; RED = False ; BLUE = False ; YELLOW = False

	elif blockType == 152: #redstone
		if RED == False:
			bulb.set_rgb(255, 0, 0)
			mc.postToChat("  Lampu berubah jadi merah!")
			GREEN = False; RED = True ; BLUE = False ; YELLOW = False

	elif blockType == 22: #lapis lazuli
		if BLUE == False:
			bulb.set_rgb(0, 0, 255)
			mc.postToChat("  Lampu berubah jadi biru!")
			GREEN = False; RED = False ; BLUE = True ; YELLOW = False
	
	elif blockType == 12: #lapis lazuli
		if YELLOW == False:
			bulb.set_rgb(255, 255, 0)
			mc.postToChat("  Lampu berubah jadi kuning!")
			GREEN = False; RED = False ; BLUE = False ; YELLOW = True
