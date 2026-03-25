from dataclasses import dataclass 
from datetime import datetime 
from typing import Optional 

@dataclass 
class WorkRecordDTO:
    emp_id: str 
    status: str 
    timestamp: datetime 
    reason: Optional[str] = None 
