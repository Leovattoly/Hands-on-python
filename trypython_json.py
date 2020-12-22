import json
#x=json.dumps([1,'Simple','list'])
file_name='file_for_trypy.txt'
with open(file_name,'w') as file_obj:
    #for i in range(10):
            i=10
            json.dump([i,'Leo Vattoly',i*i,'\n'],file_obj)
with open(file_name,'r') as file_obj:
    #for i in range(10):
    y=json.load(file_obj)
    print(y)
