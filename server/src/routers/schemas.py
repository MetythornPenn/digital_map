from pydantic import BaseModel
from datetime import datetime
from typing import List


class UserBase(BaseModel):
  username: str
  email: str
  password: str

class UserDisplay(BaseModel):
  username: str
  email: str
  class Config():
    orm_mode = True


# For PostDisplay
class User(BaseModel):
  username: str
  class Config():
    orm_mode = True

# For PostDisplay
class Comment(BaseModel):
  text: str
  username: str
  timestamp: datetime
  class Config():
    orm_mode = True
    
class PostBase(BaseModel):
  image_url: str
  image_url_type: str
  caption: str
  creator_id: int

class PostDisplay(BaseModel):
  id: int
  image_url: str
  image_url_type: str
  caption: str
  timestamp: datetime
  user: User
  comments: List[Comment]
  class Config():
    orm_mode = True

class UserAuth(BaseModel):
  id: int
  username: str
  email: str

class CommentBase(BaseModel):
  username: str
  text: str
  post_id: int
  
# ----------------------

# partner validation for create partner
class PartnerBase(BaseModel):
  id: int
  name: str
  email: str
  phone: str
  address: str
  latitude: str
  longitude: str
  category: str
  created: datetime
  image_url: str
  image_url_type: str

# promotion validation to show in list inside partner
class Promotion(BaseModel):
  name: str
  description: str
  image_url: str
  image_url_type: str
  expired: datetime
  class Config():
    orm_mode = True

# partner validation to show partner detail
class PartnerDisplay(BaseModel):
  # id: int
  name: str
  email: str
  phone: str
  address: str
  latitude: str
  longitude: str
  category: str
  image_url: str
  image_url_type: str
  promotion: List[Promotion]
  class Config():
        orm_mode = True
        

class Partner(BaseModel):
      id: int
      name: str
      class Config():
            orm_mode = True

# promotion validation for create new promotion
class PromotionBase(BaseModel):
  id: int
  name: str
  description: str
  image_url: str
  image_url_type: str
  expired: datetime
  partner_id: int 
  partner: str


class PromotionDisplay(BaseModel):
  id: str
  name: str
  description: str
  image_url: str
  image_url_type: str
  expired: datetime
  partner: Partner
  class Config():
        orm_mode = True

class Promotion(BaseModel):
      id: str
      name: str
      class Config():
            orm_mode = True

