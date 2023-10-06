from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
import datetime

from db.models import DbPromotion
from routers.schemas import PromotionBase


# def create_promotion(db: Session, request: PromotionBase):
#     new_promotion = DbPromotion(
#         name=request.name,
#         description=request.description,
#         discount=request.discount,
#         start_date=datetime.datetime.now(),
#         end_date=datetime.datetime.now() + datetime.timedelta(days=7),
#     )
#     db.add(new_promotion)
#     db.commit()
#     db.refresh(new_promotion)
#     return new_promotion
    