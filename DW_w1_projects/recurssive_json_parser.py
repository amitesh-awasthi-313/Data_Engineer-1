import json

with open(r'/home/lenovo/Desktop/Workspace/DW_w1_projects/json.json', 'r') as f:
    data = json.load(f)


def wrapper(name , parent_key = ''):
    d = {} 
    
    for i , j in name.items():
        if parent_key == ' ':
            parent_key = i 
        else :
            new_key = parent_key+'_'+i 
        if isinstance(j , dict):
            temp = wrapper(j,new_key)
            for k, v in temp.items():
                d[k] = v
        elif isinstance(j,list):
            for a,b in  enumerate(j):
                key = new_key+'_'+str(a)
                d[key] = b

       
        else:
            d[new_key] = j

    return d 

print(wrapper(data))

