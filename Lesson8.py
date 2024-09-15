student_data={'id1':
 {'name':['sara'],
  'class':['v'],
  'subject': ['english','math','science']
  } , 
  'id2':           
 {'name':['john'],
  'class':['v'],
  'subject': ['english','math','science']
  } , 
   'id3':           
{'name':['Steve'],
  'class':['v'],
  'subject': ['english','math','science']

 } ,  
   'id4':           
{'name':['Zeyad'],
  'class':['v'],
  'subject': ['english','math','science']

 } ,   
   'id5':           
{'name':['Steve'],
  'class':['v'],
  'subject': ['english','math','science']

 } ,
}
result = {}  
for key, Value in student_data.items():
    if Value not in result.values():
        result[key]= Value
print(result)
   

