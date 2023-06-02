PLACEHOLDER = "[name]"

with open("./names/invited_names.txt", mode = 'r') as file:
  names = file.readlines()
  print(names)
  

  
with open("./input/letters/startingletter.txt", mode = 'r') as letter_file:
  letter_contents = letter_file.read()
  
  for name in names:
    name = name.strip()
    new_letter = letter_contents.replace(PLACEHOLDER, name)
    print(new_letter)
    
    with open(f"./output/readytosend/letter{name}.txt", mode = "w") as file:
      file.write(new_letter)
    
    
  
  