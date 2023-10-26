import os

start_path = "."
for root, dirs, files in os.walk(start_path):
    for file in files:
        
        if file.split(".")[-1] == "js":
            print(f"{root}\\{file}")
            file_path = f"{root}\\{file}"
            # read file contents
            
            contents = ""
            with open(f"{root}\\{file}", "r") as f:
                contents = f.read()
                f.close()
            
            contents = contents.replace("localStorage.", "secureLocalStorage.")
            contents = f'''import  secureLocalStorage  from  "react-secure-storage";\n{contents} '''
            
            with open(f"{root}\\{file}", "w") as f:
                f.write(contents)


                f.close()
                
                print("updated")