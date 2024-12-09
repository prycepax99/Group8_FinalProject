from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas

def create(db: Session, feedback):
    # Create a new instance of the Feedback model with the provided data
    db_feedback = models.Feedback(
        feedback_text=feedback.feedback_text,
        rating=feedback.rating
    )
    # Add the newly created Feedback object to the database session
    db.add(db_feedback)
    # Commit the changes to the database
    db.commit()
    # Refresh the Feedback object to ensure it reflects the current state in the database
    db.refresh(db_feedback)
    # Return the newly created Feedback object
    return db_feedback

def read_all(db: Session):
    return db.query(models.Feedback).all()

def read_one(db: Session, feedback_id):
    return db.query(models.Feedback).filter(models.Feedback.id == feedback_id).first()

def update(db: Session, feedback_id, feedback):
    # Query the database for the specific feedback to update
    db_feedback = db.query(models.Feedback).filter(models.Feedback.id == feedback_id)
    # Extract the update data from the provided 'feedback' object
    update_data = feedback.model_dump(exclude_unset=True)
    # Update the database record with the new data, without synchronizing the session
    db_feedback.update(update_data, synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return the updated feedback record
    return db_feedback.first()

def delete(db: Session, feedback_id):
    # Query the database for the specific feedback to delete
    db_feedback = db.query(models.Feedback).filter(models.Feedback.id == feedback_id)
    # Delete the database record without synchronizing the session
    db_feedback.delete(synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return a response with a status code indicating success (204 No Content)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

