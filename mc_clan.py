from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()

stayed_time=0

pos=mc.player.getTilePos()
<<<<<<< HEAD
print (pos)

f = open("clanlist.csv","r")
data = f.read()
list_elements = data.split("\n")

clan_data=[]
for row in list_elements:
    split_list = row.split(',')
    clan_data.append(split_list)
roof_file_name = clan_data[1][2]

f = open(roof_file_name,"r")
=======

f = open("roof.csv","r")
>>>>>>> 0adc80597cc62da57516c7fa0ad9955c6666bee5
data = f.read()
list_elements = data.split("\n")

roof_data=[]
for row in list_elements:
    split_list = row.split(',')
    roof_data.append(split_list)

<<<<<<< HEAD
=======

>>>>>>> 0adc80597cc62da57516c7fa0ad9955c6666bee5
# Default display code
class House:
    def __init__(self):
        self.type = "csv"
# Solution code
class House:
<<<<<<< HEAD
    def __init__(self):
        self.roof_data = []
=======
    def __init__(self, roof_data):
        self.roof_data = roof_data
>>>>>>> 0adc80597cc62da57516c7fa0ad9955c6666bee5
    def buildRoof(self):
        for x in range(9):
            for z in range(9):
                if self.roof_data[x][z]=='1':
                    mc.setBlock(self.x0+8-x,self.y0+6,self.z0+8-z,1)
                else:
                    mc.setBlock(self.x0+8-x,self.y0+6,self.z0+8-z,2)
<<<<<<< HEAD
    def setRoof(self,csv_file_name):
        f = open(csv_file_name,"r")
        data = f.read()
        list_elements = data.split("\n")

        for row in list_elements:
            split_list = row.split(',')
            self.roof_data.append(split_list)

=======
>>>>>>> 0adc80597cc62da57516c7fa0ad9955c6666bee5
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

<<<<<<< HEAD
clanPoss = [[0,0,0],[10,0,0],[10,0,10],[0,0,10]]
first_house = House()
first_house.setRoof(roof_file_name)
first_house.setHousePos(pos.x,pos.y,pos.z)
second_house = House()
second_house.setRoof(clan_data[2][2])
second_house.setHousePos(pos.x+10,pos.y+10,pos.z+10)
my_clan = clan()
for house_number in range(12):
    house = House()
    clanID = int(clan_data[house_number+1][0])
    clanPosStart = clanPoss[clanID-1]
    housePosx = int(clan_data[house_number+1][3])
    housePosy = int(clan_data[house_number+1][4])
    housePosz = int(clan_data[house_number+1][5])
    house.setHousePos(pos.x+clanPosStart[0]+housePosx,pos.y+clanPosStart[1]+housePosy, pos.z+clanPosStart[2]+housePosz)
    house.setRoof(clan_data[house_number+1][2])
    my_clan.addHouse(house)

=======
first_house = House(roof_data)
first_house.setHousePos(pos.x,pos.y,pos.z)
second_house = House(roof_data)
second_house.setHousePos(pos.x+10,pos.y+10,pos.z+10)
my_clan = clan()
my_clan.addHouse(first_house)
my_clan.addHouse(second_house)
>>>>>>> 0adc80597cc62da57516c7fa0ad9955c6666bee5
my_clan.printHouses()
my_clan.buildAlls()
