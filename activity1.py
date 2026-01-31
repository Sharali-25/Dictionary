student_data = {'id1':
    {'name': ['Sharali'],
     'class': ['V'],
     'subject_intergation' : ['english,math,science']
    },
    'id2' :
    {'name': ['Siddhartha'],
     'class' : ['V'],
     'subject_intergation': ['english,math,science']
    },
    'id3':
    {'name' : ["Shayna"],
    'class' : ['V'],
    'subject_intergation' : ['english,math,science']
    },
    'id4':
    {'name' : ["Sharol"],
    'class' : ['V'],
    'subject_intergation' : ['english,math,science']
    },
}

result = {}

for key,value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)