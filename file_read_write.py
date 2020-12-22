def file_write(file_name,write_data):
    with open(file_name,'w') as file_obj:
        if file_obj.write(str(write_data))>0:
            return True
        else:
            return False

def file_read(file_name):
    with open (file_name,'r') as file_obj:
        file_content=file_obj.read()
        if file_content !='\0':
            return(file_content)
        else:
            return('unable to access the file')

file_name='file_for_trypy.txt'
file_contents='123456'
if file_write(file_name,file_contents) is True:
    print('successfully created and added the data')
else:
    print('I\'m sorry, unable to create the file')
print(file_read(file_name))
