json =  {
    "id": 1,
    "name": "Amitesh",
    "address": {
        "city": "Lucknow",
        "pin": 226010
    },
    "skills": ["Python", "SQL"],
    "company": {
        "name": "Appsquadz",
        "dept": {
            "team": "Data",
            "role": "Analyst"
        }
    }
}


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

print(wrapper(json))

