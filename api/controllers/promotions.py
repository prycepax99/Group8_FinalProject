from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas

def create(db: Session, promotion):
    # Create a new instance of the Promotion model with the provided data
    db_promotion = models.Promotion(
        promotion_name=promotion.promotion_name,
        discount=promotion.discount
    )
    # Add the newly created Promotion object to the database session
    db.add(db_promotion)
    # Commit the changes to the database
    db.commit()
    # Refresh the Promotion object to ensure it reflects the current state in the database
    db.refresh(db_promotion)
    # Return the newly created Promotion object
    return db_promotion

def read_all(db: Session):
    return db.query(models.Promotion).all()

def read_one(db: Session, promotion_id):
    return db.query(models.Promotion).filter(models.Promotion.id == promotion_id).first()

def update(db: Session, promotion_id, promotion):
    # Query the database for the specific promotion to update
    db_promotion = db.query(models.Promotion).filter(models.Promotion.id == promotion_id)
    # Extract the update data from the provided 'promotion' object
    update_data = promotion.model_dump(exclude_unset=True)
    # Update the database record with the new data, without synchronizing the session
    db_promotion.update(update_data, synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return the updated promotion record
    return db_promotion.first()

def delete(db: Session, promotion_id):
    # Query the database for the specific promotion to delete
    db_promotion = db.query(models.Promotion).filter(models.Promotion.id == promotion_id)
    # Delete the database record without synchronizing the session
    db_promotion.delete(synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return a response with a status code indicating success (204 No Content)
    return Response(status_code=status.HTTP_204_NO_CONTENT)