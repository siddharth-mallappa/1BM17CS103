class CallDetails:
    def __init__(self,f_phno,t_phno,duration,typ):
        self.f_phno=f_phno
        self.t_phno=t_phno
        self.duration=duration
        self.typ=typ

    def getter(self):
        return (self.f_phno,self.t_phno,self.duration,self.typ)
    

class Util:
    def __init__(self):
        self.list_of_call_objects=[]

    def parse_customer(self,list_of_call_string):
        for x in list_of_call_string:
            a=x.split(",")
            call=CallDetails(a[0],a[1],a[2],a[3])
            self.list_of_call_objects.append(call)
    def output(self):
        c1,c2,c3=0,0,0
        for x in self.list_of_call_objects:
            print(x.getter())
            if(x.getter()[3]=='STD'):
                c1+=1
            elif(x.getter()[3]=='ISD'):
                c2+=1
            else:
                c3+=1

        print("STD=",c1)
        print("ISD=",c2)
        print("LOCAL=",c3) 
            
       
call='9901290,9090129,23,STD'
call2='990134290,909430129,23,ISD'
call3='990123490,902390129,23,local'
call4='990123490,902390129,23,local'
list_of_call_string=[call,call2,call3,call4]
util=Util()
util.parse_customer(list_of_call_string)
util.output()
