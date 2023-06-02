with open("./names/invited_names.txt", mode = 'r') as file:
  namelist = file.readlines()
  print(namelist)
for i in range(len(namelist)):
  with open("./input/letters/startingletter.txt", mode = 'r') as file:
    letterfirstline = file.readlines(1)
    letterlines = file.readlines()
    print(letterfirstline)
    print(letterlines)
    str = letterfirstline[0]
    print(str)
    
    up_str = str.replace("[name]",f"{namelist[i].strip()}")
    print(up_str)
    
  
  with open(f"./output/readytosend/letter{namelist[i]}.txt", mode = "w") as file:
    file.write(f"{up_str}")
    for j in letterlines:
      file.write(j)
  
  