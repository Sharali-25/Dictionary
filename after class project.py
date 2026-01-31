student_data = {'ida':
    {'name': ['skibidi'],
     'class': ['7'],
     'subject' : ['english,math,science']
    },
    'idb' :
    {'name': ['bhupendra jogi'],
     'class' : ['8']
     'subject': ['art,theatre']
    },
    'idc':
    {'name' : ["Saniya"],
    'class' : ['4'],
    'subject' : ['math,music']
    },
    'idd':
    {'name' : ["Ankita maam"],
    'class' : ['9'],
    'subject' : ['geometry,english,pe']
    },
}

result = {}

for key,value in student_data.items():
    if value not in result.vlues():
        result[key] = value

print(result)