
from typing import Optional
from pydantic import BaseModel

class Test(BaseModel):
    id: Optional[int]
    FL_DATE : Optional[str]
    AIRLINE_ID : Optional[int]
    ORIGIN_AIRPORT_ID : Optional[int]
    DEST_AIRPORT_ID : Optional[int]
    DEP_TIME: Optional[str]