from pydantic import BaseModel
from typing import Optional

class MarketingRequest(BaseModel):
    region: str
    product: str
    event: str
    image: Optional[str] = None
