class Student:
    school="Akirachix"
    def __init__(self,first_name,last_name,age,country):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.country=country
        self.year=2025-age
    
    def greet_student(self):
        return f"Hello {self.name}, welcome to ,{self.school}."
    def initials(self):
        # return f"Hello {self.name}, welcome to ,{self.school}."
        first_name=self.first_name.split() 
        last_name=self.last_name.split()
        initials=""
        # initial=""
        for name in first_name:
            initials+= name[0].upper()
            # return f"Hello {self.first_name}.{self.last_name}"
            return initials
        for name in last_name:
            initial+= name[0].upper() 
            return initial
    def marks(self,points):
        self.marks.append(points)
        total=0
        for num in nums:
            total+=points

            return f"Marks recorded. Totals marks {total}"
        

        
    