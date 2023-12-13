import os

folders = input("Please provide the folders name with space in between folder name: ").split()

for folder in folders:
    try: 
      files = os.listdir(folder)
    except FileNotFoundError:
        print("Please provide the valid file name instead of ==>" + folder)
        continue

    print("List out the available files in the current directory ==> " + folder)

    for file in files:
       print(file)



