class User:
    def __init__(self,name: str, password: str, email:str):
        self.name= name
        self.__password= password #private
        self.__email=email #private

    def Register(self,Registered_Users)->bool:
        for user in Registered_Users:
            if user._email == self._email:
                return False
        Registered_Users.append(self)
        return True
   
    def login(self, registered_users):
        return self in registered_users
   
    def get_name(self)->str:
        return self.name

    def set_name(self,name:str)->None:
        self.name = name
    
    def get_password(self)->str:
        return self.__password
    
    def set_password(self,password:str)->None:
        self.__password = password

    def get_email(self)->str:
        return self.__email
    
    def set_email(self,email:str)->None:
        self.__email = email
