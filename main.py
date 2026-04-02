def register():
    print('----REGISTER----')
    name=input('Enter name --->')
    password=input('Enter password -->')
    ll=[]
    for i in  ll:
        with open('users.txt','r') as file:
            i=file.readline()
            i.split(':')
        if len(i)>=0 and i[0]==name:
            print('ZAYNITAY')
        return False
    with open('users.txt','a') as file:
        file.write(f'{name}: {password}\n')
        print('Welcome')
    return True
m=register()
print(m)            