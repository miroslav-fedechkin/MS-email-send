from typing import List
from pydantic import EmailStr, BaseModel

class EmailShema(BaseModel):
    email: List[EmailStr]
    