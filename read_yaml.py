import os
import yaml

with open('folders.yaml') as f:
    
    docs = yaml.load_all(f, Loader=yaml.FullLoader)

    for doc in docs:      
        for k, v in doc.items():
            root_dir = k
            sub_dirs = v
            for i in range(len(sub_dirs)):
                dir_name = f"{root_dir}/{sub_dirs[i]}"

                try:
                    os.makedirs(dir_name)
                    print(f"Directory {dir_name} created.")
                except FileExistsError:
                    print(f"Directory {dir_name} exists.")
                