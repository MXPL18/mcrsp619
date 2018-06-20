import binvox_rw
import mcpi.block as block
import mcpi.vec3  as vec3
from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()

pos=vec3.Vec3()

pos.x = 9
pos.y = 15
pos.z = 102
clanPoss = [[0,0,0],[60,0,0],[60,0,60],[0,0,60]]
logoPoss=[[10,0,20],[10,0,20],[10,0,20],[10,0,20]]

logobinvox=["donut.binvox","guidaopao.binvox","mickey__mouse_hoofd.binvox","nanhun.binvox"]

mc.setBlocks(pos.x-10,pos.y,pos.z-10,pos.x+200,pos.y+40,pos.z+200,0)
#mc.setBlocks(pos.x-10,pos.y-1,pos.z-10,pos.x+120,pos.y,pos.z+120,1)

f = open("clanlist.csv","r")
data = f.read()
list_elements = data.split("\n")
clan_data=[]

for row in list_elements:
    split_list = row.split(',')
    clan_data.append(split_list)

class House:
    def __init__(self):
        self.roof_data = []
        self.xl=9
        self.zl=9
        self.yl=6

    def setRoof(self,csv_file_name):
        f = open(csv_file_name,"r")
        data = f.read()
        list_elements = data.split("\n")
        self.xl=len(list_elements)-1
        self.zl=0
        x=0
        for row in list_elements:
            split_list = row.split(',')
            if self.zl < len(split_list):
                self.zl = len(split_list)
            z=0
            for tile in split_list:
                if tile =='1':
                    mc.setBlock(self.x0+x,self.y0+self.yl,self.z0+z,89)
                else:
                    mc.setBlock(self.x0+x,self.y0+self.yl,self.z0+z,2)
                z=z+1
            x=x+1

    def buildWindows(self):
        print("dummy build windows TBD")
    def setHousePos(self, x,y,z):
        self.x0 = x
        self.y0 = y
        self.z0 = z
    def buildHouse(self):
        x0 = self.x0
        y0 = self.y0
        z0 = self.z0
        for y in range(self.yl):
            for x in range(self.xl):
                mc.setBlock(x0+x,y0+y,z0,89)
                mc.setBlock(x0+x,y0+y,z0+self.zl,89)
            for z in range(self.zl):
                mc.setBlock(x0,y0+y,z0+z,89)
                mc.setBlock(x0+self.xl,y0+y,z0+z,89)
    def buildAll(self):
        self.buildHouse()
        self.buildWindows()

class clan:
    def __init__(self,pos):
        self.houses = []
        self.pos=pos
        self.logopos=pos
    def setlog(self,pos,logoname):
        self.logopos[0]=self.pos[0]+pos[0]
        self.logopos[1]=self.pos[1]+pos[1]
        self.logopos[2]=self.pos[2]+pos[2]
        self.logoname=logoname
    def addHouse(self,house):
        self.houses.append(house)
    def printHouses(self):
        for house in self.houses:
            print (house.x0,house.y0,house.z0)
    def buildclanlogo(self):
        print("I will build clan logo")
        print(self.logoname)
        x0=self.logopos[0]
        y0=self.logopos[1]
        z0=self.logopos[2]
        print(x0,y0,z0)
        with open(self.logoname, 'rb') as f:
            model = binvox_rw.read_as_3d_array(f)
            print(model.dims)
            print(model.scale)
            print(model.translate)
            #print(model.data)
        for y in range(model.dims[1]):
            #print("layer y=",y)
            layer_data=model.data[y]
            stringlayer=""
            for x in range(model.dims[0]):
                stringlayer=stringlayer+"\n"
                for z in range(model.dims[2]):
                    if model.data[x][z][y] == True:
                        stringlayer=stringlayer+'1'
                        mc.setBlock(x0+x,y0+y,z0+z,89)
                    else:
                        stringlayer=stringlayer+'0'
                        mc.setBlock(x0+x,y0+y,z0+z,block.AIR.id)
                #print(stringlayer）
        time.sleep(5)
    def buildAlls(self):
        self.buildclanlogo()
        for house in self.houses:
            house.buildAll()

myclanlist=[]
for cid in range(4):
    cp=clanPoss[cid]
    my_clan = clan([cp[0]+pos.x,cp[1]+pos.y,cp[2]+pos.z])
    my_clan.setlog(logoPoss[cid],logobinvox[cid])
    myclanlist.append(my_clan)

for house_number in range(12):
    house = House()
    clanID = int(clan_data[house_number+1][0])
    clanPosStart = clanPoss[clanID-1]
    housePosx = int(clan_data[house_number+1][3])
    housePosy = int(clan_data[house_number+1][4])
    housePosz = int(clan_data[house_number+1][5])
    house.setHousePos(pos.x+clanPosStart[0]+housePosx,pos.y+clanPosStart[1]+housePosy, pos.z+clanPosStart[2]+housePosz)
    house.setRoof(clan_data[house_number+1][2])
    myclanlist[clanID-1].addHouse(house)

for my_clan in myclanlist:
    my_clan.printHouses()
    my_clan.buildAlls()
print("finish clan building")
    
