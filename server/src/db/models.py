from sqlalchemy.sql.schema import ForeignKey
from .database import Base
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime



class DbUser(Base):
  __tablename__ = 'user'
  id = Column(Integer, primary_key=True, index=True)
  username = Column(String)
  email = Column(String)
  password = Column(String)
  items = relationship('DbPost', back_populates='user')

class DbPost(Base):
  __tablename__ = 'post'
  id = Column(Integer, primary_key=True, index=True)
  image_url = Column(String)
  image_url_type = Column(String)
  caption = Column(String)
  timestamp = Column(DateTime)
  user_id = Column(Integer, ForeignKey('user.id'))
  user = relationship('DbUser', back_populates='items')
  comments = relationship('DbComment', back_populates='post')

class DbComment(Base):
  __tablename__ = 'comment'
  id = Column(Integer, primary_key=True, index=True)
  text = Column(String)
  username = Column(String)
  timestamp = Column(DateTime)
  post_id = Column(Integer, ForeignKey('post.id'))
  post = relationship("DbPost", back_populates="comments")
  
  
# create partner class with id, name, email, phone, address, latitude, longtitue, category, created, updated_at, image
class DbPartner(Base):
  __tablename__= 'partner'
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String)
  email = Column(String)
  phone = Column(String)
  address = Column(String)
  latitude = Column(String)
  latitude = Column(String)
  category = Column(String)
  created = Column(DateTime, default=datetime.utcnow)
  # updated_at = Column(DateTime)
  image_url = Column(String)
  image_url_type = Column(String)
  promotion = relationship('DbPromotion', back_populates='partner')

# create promotion class with id, name, description, image, created, expired
class DbPromotion(Base):
  __tablename__ = 'promotion'
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String)
  description = Column(String)
  discount = Column(Float)
  image_url = Column(String)
  image_url_type = Column(String)
  created = Column(DateTime, default=datetime.utcnow)
  expired = Column(DateTime)
  partner_id = Column(Integer, ForeignKey('partner.id'))
  partner = relationship('DbPartner', back_populates='promotion')
  