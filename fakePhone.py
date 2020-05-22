import random
class rand:
    def __init__(self):
        self.phone = None
        self.name = None
    def fake(self):
        listPhoneStart = [
            '086','096','097','098','032','033','034','035','036','037','038','039','090','093','091','094','083','084','085',
        ]
        start = random.choice(listPhoneStart)
        #random 7 number from 0000000 to 9999999
        end = random.randint(0000000, 9999999)
        self.phone = start + str(end)
        return self.phone
    def randomName(self):
        s=open("name.txt","r")
        m=s.readlines()
        l=[]
        for i in range(0,len(m)-1):
            x=m[i]
            z=len(x)
            a=x[:z-1]
            l.append(a)
        l.append(m[i+1])
        self.name =random.choice(l)
        s.close()
        return self.name

class seed:
    pass
if __name__ == '__main__':
    for i in range(0, 10):
        p = rand()
        phone = p.fake()
        name = p.randomName()
        print(name)
        print(phone)