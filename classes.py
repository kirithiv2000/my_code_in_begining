class family:
    def family(self):
        self.mom="Govindhammal.K"
        self.dad="Ramakrishna.K.R"
        self.brother="Megananthan.R"
        print(self.dad,",\n",self.mom,",\n",self.brother)

class about_self(family):
    def __init__(self):
        import datetime
        self.name="Kirithiv.R"
        self.nationality="Indian"
        self.district="Tamil Nadu"
        self.state="Salem"
        self.birth=datetime.date(2000,6,21)
        self.arrived_to_navgurukul=datetime.date(2019,6,20)
        today=datetime.date.today()
        self.today=today

    def age(self):
        age1=self.today-self.birth
        return age1.days//365

class daily_plan(about_self):
    def list(self):
        self.l=[]
    def append(self,a):
        self.l.append(a)
    def displaylist(self):
        print(self.l)

class navgurukul(daily_plan):
    def days_completed_in_navgurukul(self):
        days=self.today-self.arrived_to_navgurukul
        self.days_completed_in_navgurukul=days
        return days.days

    def months_completed_in_navgurukul(self):
        month=self.days_completed_in_navgurukul.days//30
        remaining_days=self.days_completed_in_navgurukul.days%31
        g=str(month)+" months "+str(remaining_days)+" days "
        return g

a=navgurukul()
print(a.name)
print(a.birth)
print(a.arrived_to_navgurukul)
print(a.nationality)
print(a.state)
print(a.district)
print(a.age())
print(a.days_completed_in_navgurukul())
print(a.months_completed_in_navgurukul())
a.family()

a.list()
a.append("bun'twell uhv ocnfi dance iatfuw iudn'twtd udn't do nus")
a.displaylist()

a.list()
a.append("list hmpln 14-10-2019")
a.append("watits")
a.append("hmdwtttc")
a.displaylist()

a.list()
a.append("Write GBU 13-10-2019")
a.append("Not yet done")
a.displaylist()

a.list()
a.append("start recursion project")
a.append("Not yet done")
a.displaylist()

a.list()
a.append("finish recursion project")
a.append("Not yet done")
a.displaylist()

a.list()
a.append("start web scraping project")
a.append("Not yet done")
a.displaylist()

a.list()
a.append("finish web scraping project")
a.append("Not yet done")
a.displaylist()

print(vars(a))

class students:
    def dict(self):
        d={}
        self.d=d

    def da(self,a,b):
        self.d[a]=b
    def displaydict(self):
        for i,j in zip(self.d,self.d.values()):
            print(i+" - "+str(j))

Ng=students()
Ng.dict()
Ng.da("kirithiv",1)
Ng.da("biju",2)
Ng.da("paranthaman",3)
Ng.da("ajith",4)
Ng.da("yogesh",5)
Ng.da("biju",6)
Ng.da("tapas",7)
Ng.da("rakesh",8)
Ng.da("sabid",9)
Ng.da("nayak",10)
Ng.da("rahit",11)
Ng.da("vishal",12)
Ng.da("mohit",13)
Ng.da("deepak",14)
Ng.da("deepash",15)
Ng.da("prathik",16)
Ng.da("tarique",17)
Ng.da("aman",18)
Ng.da("sanjay",19)
Ng.da("himanshu",20)
Ng.da("jai prakash",21)
Ng.da("arjun",22)
Ng.da("anand",23)
Ng.da("kapil",24)
Ng.da("sahid",25)
Ng.da("vivek",26)
Ng.da("bhavanesh",27)
Ng.da("",28)
Ng.da("biju",29)
Ng.da("biju",30)
Ng.da("biju",31)
Ng.da("biju",32)
Ng.da("biju",33)
Ng.da("biju",34)
Ng.da("biju",35)
Ng.da("biju",36)
Ng.da("biju",37)
Ng.da("biju",38)
Ng.da("biju",39)
Ng.da("biju",40)
Ng.da("biju",41)
Ng.da("biju",42)
Ng.da("biju",43)
Ng.da("biju",44)
Ng.da("biju",45)
Ng.da("biju",46)
Ng.displaydict()






def __add__(a,b):
    if type(a)==



