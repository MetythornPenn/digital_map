from auth.oauth2 import get_current_user
from fastapi import APIRouter, Depends, status, UploadFile, File
from fastapi import HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
# from db import db_partner
from controllers import partner 
from routers.schemas import Partner, PartnerBase, PartnerDisplay

from typing import List
import random
import string
import shutil

router = APIRouter(
    prefix= '/partner',
    tags= ['partner']
)


image_url_types = ['absolute', 'relative']


# create new partner route
@router.post('', response_model=PartnerDisplay)
def create_partner(request: PartnerBase):
    if not request.image_url_type in image_url_types:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, 
                detail="Parameter image_url_type can only take values 'absolute' or 'relative'.")
    return partner.create_partner(request)


# get all partners route
@router.get('', response_model=List[PartnerDisplay])
def get_partners(db: Session = Depends(get_db)):
    return partner.get_all(db)


# upload image to partners
@router.post('/image')
def upload_image(image: UploadFile = File(...)):
    letters = string.ascii_letters
    rand_str = ''.join(random.choice(letters) for i in range(6))
    new = f'_{rand_str}.'
    filename = new.join(image.filename.rsplit('.', 1))
    path = f'images/partners/{filename}'
    
    with open(path, "w+b") as buffer:
        shutil.copyfileobj(image.file, buffer)
    
    return {'filename': path}


# delete partner route
@router.delete('/{id}')
def delete_partner(id: int, db: Session = Depends(get_db)):
    return partner.delete(db, id)



