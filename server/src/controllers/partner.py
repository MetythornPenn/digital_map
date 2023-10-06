from fastapi import HTTPException, status
from db.models import DbPartner
from routers.schemas import PartnerBase
from sqlalchemy.orm import Session
from datetime import datetime

# create new partner function
def create_partner(request: PartnerBase, db: Session):
    new_partner = DbPartner(
        name = request.name,
        email = request.email,
        phone = request.phone,
        address = request.address,
        latitude = request.latitude,
        longitude = request.longitude,
        category = request.category,
        created = datetime.now(),
        image_url = request.image_url,
        image_url_type = request.image_url_type,
        # promotion = request.promotion,
    )
    db.add(new_partner)
    db.commit()
    db.refresh(new_partner)
    return new_partner

# get all partner function
def get_all(db: Session):
    return db.query(DbPartner).all()


# update partner function
def update_partner(id: int, request: PartnerBase, db: Session):
    partner = db.query(DbPartner).filter(DbPartner.id == id)
    if not partner.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Partner with id {id} not found')
    # ...
    
    # update if exist
    partner.update(request.dict())
    db.commit()
    return 'ok'

# delete partner function
def delete_partner(id: int, db: Session, partner_id: int):
    partner = db.query(DbPartner).filter(DbPartner.id == id).first()
    
    if not partner:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Partner with id {id} not found')
        
    # if partner.id != partner_id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
    #                         detail=f'Only partner creator can delete partner')
        
    db.delete(partner)
    db.commit()
    return 'ok'
