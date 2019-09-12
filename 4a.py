class student :
    def __init__(self,s_id,age,marks):
        self.s_id=s_id
        if self.validate_age(age) and self.validate_marks(marks):
            print("Qualified")
            print("Sudent age",self.__age)
            print("Student marks",self.__marks)
        else :
            print("Not qualified")

        
    def get_id(self):
        return self.s_id
    def get_age(self):
        return self.__age
    def get_marks(self):
        return self.__marks           
        
   


    def validate_age(self,age):
        self.__age=age
        if age>20 :
            return True 
        else :
            return False

    def validate_marks(self,marks ):
        self.__marks=marks
        if marks>65:
            return True
        else :
            return False

obj = student(112,20,90)
print("Sudent id:",obj.get_id())
