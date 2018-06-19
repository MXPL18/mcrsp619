f = open("clanlist.csv","r")
data = f.read()
list_elements = data.split("\n")

clan_data=[]
for row in list_elements:
    split_list = row.split(',')
    clan_data.append(split_list)
roof_file_name = clan_data[1][2]

f = open(roof_file_name,"r")
data = f.read()
list_elements = data.split("\n")

roof_data=[]
for row in list_elements:
    split_list = row.split(',')
    roof_data.append(split_list)
