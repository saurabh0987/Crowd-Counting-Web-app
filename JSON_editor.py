import json
import torch
"""
with open('part_B_val.json') as f:
    data = json.load(f)

print(data)
print(len(data[0])-10)

#print(len(data[0])-len(data[0][-10:]))
for ls in range(len(data)):
    x=len(data[ls])-62
    data[ls] ='E:\\New folder\\ShanghaiTech_Crowd_Counting_Dataset\\part_B_final\\train_data\\images\\'+data[ls][-x:]
print(data)

with open('part_B_val_1.json','w') as f:
    json.dump(data,f)
"""
print(torch.cuda.is_available())




