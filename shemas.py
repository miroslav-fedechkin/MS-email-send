from typing import List
from pydantic import EmailStr, BaseModel

class EmailShema(BaseModel):
    to_email: List[EmailStr]
    