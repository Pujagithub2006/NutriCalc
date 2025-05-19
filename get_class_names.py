import os

dataset_dir = r'C:\Users\91901\OneDrive\Desktop\Food Set\train_set'  # must be the same structure used during training
class_labels = sorted(os.listdir(dataset_dir))  # sort ensures consistent order

for i, label in enumerate(class_labels):
    print(f"{i}: {label}")
    

