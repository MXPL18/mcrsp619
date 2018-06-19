from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()

stayed_time=0

pos=mc.player.getTilePos()

f = open("roof.csv","r")
data = f.read()
list_elements = data.split("\n")

roof_data=[]
for row in list_elements:
    split_list = row.split(',')
    roof_data.append(split_list)


# Default display code
class House:
    def __init__(self):
        self.type = "csv"
# Solution code
class House:
    def __init__(self, roof_data):
        self.roof_data = roof_data
    def buildRoof(self):
        for x in range(9):
            for z in range(9):
                if self.roof_data[x][z]=='1':
                    mc.setBlock(self.x0+8-x,self.y0+6,self.z0+8-z,1)
                else:
                    mc.setBlock(self.x0+8-x,self.y0+6,self.z0+8-z,2)
    def buildWindows(self):
        for x in range (7):
            for z in range (7):
                if self.roof_data[x][z]=='1':
                    mc.setBlock(self.x0+8-x,self.y0+2,self.z0+8-z,102)
    def setHousePos(self, x,y,z):
        self.x0 = x
        self.y0 = y
        self.z0 = z
    def buildHouse(self):
        x0 = self.x0
        y0 = self.y0
        z0 = self.z0
        for x in range(9):
            mc.setBlock(x0+x,y0,z0,89)
        for z in range(9):
            mc.setBlock(x0,y0,z0+z,89)
        for y in range(7):
            mc.setBlock(x0,y0+y,z0,89)

        for x in range(9):
            for y in range (7):
                mc.setBlock(x0+x,y0+y,z0,89)
        for x in range(9):
            for z in range(9):
                mc.setBlock(x0+x,y0,z0+z,89)
        for z in range(9):
            for y in range(7):
                mc.setBlock(x0,y0+y,z0+z,89)

        x1 = x0+8
        y1 = y0+6
        z1 = z0+8
        for x in range(9):
            mc.setBlock(x1-x,y1,z1,89)
        for z in range(9):
            mc.setBlock(x1,y1,z1-z,89)
        for y in range(7):
            mc.setBlock(x1,y1-y,z1,89)

        for x in range(9):
            for y in range (7):
                mc.setBlock(x1-x,y1-y,z1,89)
        for x in range(9):
            for z in range(9):
                mc.setBlock(x1-x,y1,z1-z,89)
        for z in range(9):
            for y in range(7):
                mc.setBlock(x1,y1-y,z1-z,89)
    def buildAll(self):
        self.buildHouse()
        self.buildRoof()
        self.buildWindows()

class clan:
    def __init__(self):
        self.houses = []
    def addHouse(self,house):
        self.houses.append(house)
    def printHouses(self):
        for house in self.houses:
            print (house.x0,house.y0,house.z0)
    def buildAlls(self):
        for house in self.houses:
            house.buildAll()

first_house = House(roof_data)
first_house.setHousePos(pos.x,pos.y,pos.z)
second_house = House(roof_data)
second_house.setHousePos(pos.x+10,pos.y+10,pos.z+10)
my_clan = clan()
my_clan.addHouse(first_house)
my_clan.addHouse(second_house)
my_clan.printHouses()
my_clan.buildAlls()
