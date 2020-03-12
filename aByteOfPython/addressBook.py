import pickle
import os

contactFile=r"C:\Users\EGXXJXX\OneDrive - ODMAIL\123\doc\backup\PycharmProjects\aByteOfPython\addressbook.data"
if os.path.exists(contactFile):
    with open(contactFile,'rb') as f:
        contact=pickle.load(f)
else:
    contact={}


class People:

    myContact=contact

    def __init__(self,name,email="",phone="",tag=""):
        self.name=name
        self.email=email
        self.phone=phone
        self.tag=tag

    @classmethod
    def browse(self):
        li=sorted(People.myContact.items())
        for i in li:
            print("name: ",i[0],",email: ",i[1][0],",phone: ",i[1][1],",tag: ",i[1][2])


    def add(self):
        if self.name in People.myContact :
            print(self.name,"in the address book! will modify,the old one is:")
            print("name: ",self.name,
                  ",email: ",People.myContact[self.name][0],
                  ",phone: ",People.myContact[self.name][1],
                  ",tag: ",People.myContact[self.name][2])
        else :
            print(self.name,"not in address book! will add")
        People.myContact[self.name]=[self.email,self.phone,self.tag]

    def delete(self):
        if self.name in People.myContact:
            del People.myContact[self.name]
        else :
            print(self.name,"not in address book!will do nothing!")

    def search(self):
        if self.name in People.myContact:
            print("name: ",self.name,
                  ",email: ",People.myContact[self.name][0],
                  ",phone: ",People.myContact[self.name][1],
                  ",tag: ",People.myContact[self.name][2])
        else:
            print(self.name,"not find in the address book!")


action=["a","m","d","s","b","l"]

while True:
    print("================================python cli address book================================")
    print("you can add(a),modify(m),delete(d),searh(s),browse(b),leave(l) you address book: ")
    move = input("please input a move:")
    if move not in action:
        move = input("wrong action,please input a move:")
    elif move=="a" or move=="m":
        people=People(input("name= "),input("email= "),input("phone= "),input("tag= "))
        people.add()
    elif move=="d":
        people=People(input("name= "))
        people.delete()
    elif move=="s":
        people = People(input("name= "))
        people.search()
    elif move=="b":
        People.browse()
    elif move=="l":
        break

with open (contactFile,'wb') as f:
    pickle.dump(People.myContact,f)






