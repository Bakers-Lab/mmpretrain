# 用于将hot盘中的分组的nonphone数据合并到一起

import os
import shutil
from tqdm import tqdm 
class NonPhoneMerge:
    def __init__(self,root:str,out:str) -> None:
        self.root=root
        self.outpath=out
        
    def merge(self,):
        folder_name=self.root
        subdirectories = [d for d in os.listdir(folder_name) if os.path.isdir(os.path.join(folder_name, d))]
        folders = list(filter(lambda x: 'Group' in x, subdirectories))
        folders_train=[os.path.join(self.root,folder,'train') for folder in folders]
        folders_val=[os.path.join(self.root,folder,'val') for folder in folders]
        file_all=[]
        for train_folder in folders_train:
            file_all+=[os.path.join(train_folder,file_name) for file_name in os.listdir(train_folder)]
        for val_folder in folders_val:
            file_all+=[os.path.join(val_folder,file_name) for file_name in os.listdir(val_folder)]
        img_files=list(filter(lambda x: '.jpg' in x, file_all))
        for img in tqdm(img_files):
            shutil.copy(img,self.outpath)
    
if __name__=="__main__":
    # 直接写变量 比较简答用的也少 不写参数解析了
    
    root="/archive/hot4/Nonphone/0914BKS"
    nonphonemerge=NonPhoneMerge(root=root,out="/archive/hot4/self-nonphone")
    nonphonemerge.merge()