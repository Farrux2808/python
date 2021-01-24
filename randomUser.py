import requests

usersData = []
i=0
gender = 'male'
open("usersData.txt","w",encoding='utf-8').close()
while(i<20):
    if i==10:
        gender = 'female'
    r = requests.get('https://randomuser.me/api/?inc=name,dob,location,gender&gender='+gender)
    print(r.status_code)
    if r.status_code == 200:
        x = r.json()
        x = x['results'][0]
        data = {
            "fullName" : x['name']['first'] + " " + x['name']['last'],
            "city" : x['location']['city'],
            "age" : x['dob']['age']
        }
        usersData.append(data)
        i+=1
usersFile = open("usersData.txt","a",encoding='utf-8')
for user in usersData:
    usersFile.write(str(user))
    usersFile.write("\n")
usersFile.close()
print('success')

    
