from pydantic import BaseModel

class SUser(BaseModel):
    password: str
    name:str
    
    class Config:
        from_atributes=True
        
class SUpdate(BaseModel):
    password:str
    
    class Config:
        from_atributes=True