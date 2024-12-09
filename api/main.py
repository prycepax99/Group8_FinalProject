from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from .models import models, schemas
from .controllers import orders, order_details, recipes, resources, sandwiches, promotions, feedbacks
from .dependencies.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Order CRUD
@app.post("/orders/", response_model=schemas.Order, tags=["Orders"])
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return orders.create(db=db, order=order)


@app.get("/orders/", response_model=list[schemas.Order], tags=["Orders"])
def read_orders(db: Session = Depends(get_db)):
    return orders.read_all(db)


@app.get("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def read_one_order(order_id: int, db: Session = Depends(get_db)):
    order = orders.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order


@app.put("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def update_one_order(order_id: int, order: schemas.OrderUpdate, db: Session = Depends(get_db)):
    order_db = orders.read_one(db, order_id=order_id)
    if order_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.update(db=db, order=order, order_id=order_id)


@app.delete("/orders/{order_id}", tags=["Orders"])
def delete_one_order(order_id: int, db: Session = Depends(get_db)):
    order = orders.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.delete(db=db, order_id=order_id)









# OrderDetail CRUD
@app.post("/order_details/", response_model=schemas.OrderDetail, tags=["OrderDetails"])
def create_order_detail(order_detail: schemas.OrderDetailCreate, db: Session = Depends(get_db)):
    return order_details.create(db=db, order_detail=order_detail)

@app.get("/order_details/", response_model=list[schemas.OrderDetail], tags=["OrderDetails"])
def read_order_details(db: Session = Depends(get_db)):
    return order_details.read_all(db)

@app.get("/order_details/{order_detail_id}", response_model=schemas.OrderDetail, tags=["OrderDetails"])
def read_one_order_detail(order_detail_id: int, db: Session = Depends(get_db)):
    order_detail = orders.read_one(db, order_id=order_detail_id)
    if order_detail is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order_detail

@app.put("/order_details/{order_detail_id}", response_model=schemas.OrderDetail, tags=["OrderDetails"])
def update_one_order_detail(order_detail_id: int, order_detail: schemas.OrderDetailUpdate, db: Session = Depends(get_db)):
    order_detail_db = order_details.read_one(db, order_id=order_detail_id)
    if order_detail_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order_details.update(db=db, order_detail=order_detail, order_id=order_detail_id)

@app.delete("/order_details/{order_detail_id}", tags=["OrderDetails"])
def delete_one_order_detail(order_detail_id: int, db: Session = Depends(get_db)):
    order_detail = order_details.read_one(db, order_id=order_detail_id)
    if order_detail is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order_details.delete(db=db, order_id=order_detail_id)







# Recipe CRUD
@app.post("/recipes/", response_model=schemas.Recipe, tags=["Recipes"])
def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    return recipes.create(db=db, recipe=recipe)

@app.get("/recipes/", response_model=list[schemas.Recipe], tags=["Recipes"])
def read_recipes(db: Session = Depends(get_db)):
    return recipes.read_all(db)

@app.get("/recipes/{recipe_id}", response_model=schemas.Recipe, tags=["Recipes"])
def read_one_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = recipes.read_one(db, recipe_id=recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="User not found")
    return recipe

@app.put("/recipes/{recipe_id}", response_model=schemas.Recipe, tags=["Recipes"])
def update_one_recipe(recipe_id: int, recipe: schemas.RecipeUpdate, db: Session = Depends(get_db)):
    recipe_db = recipes.read_one(db, recipe_id=recipe_id)
    if recipe_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return recipes.update(db=db, recipe=recipe, recipe_id=recipe_id)

@app.delete("/recipes/{recipe_id}", tags=["Recipes"])
def delete_one_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = recipes.read_one(db, recipe_id=recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="User not found")
    return recipes.delete(db=db, recipe_id=recipe_id)

# Resource CRUD
@app.post("/resources/", response_model=schemas.Resource, tags=["Resources"])
def create_resource(resource: schemas.ResourceCreate, db: Session = Depends(get_db)):
    return resources.create(db=db, resource=resource)

@app.get("/resources/", response_model=list[schemas.Resource], tags=["Resources"])
def read_resources(db: Session = Depends(get_db)):
    return resources.read_all(db)

@app.get("/resources/{resource_id}", response_model=schemas.Resource, tags=["Resources"])
def read_one_resource(resource_id: int, db: Session = Depends(get_db)):
    resource = resources.read_one(db, resource_id=resource_id)
    if resource is None:
        raise HTTPException(status_code=404, detail="User not found")
    return resource

@app.put("/resources/{resource_id}", response_model=schemas.Resource, tags=["Resources"])
def update_one_resource(resource_id: int, resource: schemas.ResourceUpdate, db: Session = Depends(get_db)):
    resource_db = orders.read_one(db, order_id=resource_id)
    if resource_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return resources.update(db=db, resource=resource, resource_id=resource_id)

@app.delete("/resources/{resource_id}", tags=["Resources"])
def delete_one_resource(resource_id: int, db: Session = Depends(get_db)):
    resource = resources.read_one(db, resource_id=resource_id)
    if resource is None:
        raise HTTPException(status_code=404, detail="User not found")
    return resources.delete(db=db, resource_id=resource_id)







# Sandwich CRUD
@app.post("/sandwiches/", response_model=schemas.Sandwich, tags=["Sandwiches"])
def create_sandwich(sandwich: schemas.SandwichCreate, db: Session = Depends(get_db)):
    return sandwiches.create(db=db, sandwich=sandwich)

@app.get("/sandwiches/", response_model=list[schemas.Sandwich], tags=["Sandwiches"])
def read_sandwiches(db: Session = Depends(get_db)):
    return sandwiches.read_all(db)

@app.get("/sandwiches/{sandwich_id}", response_model=schemas.Sandwich, tags=["Sandwiches"])
def read_one_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    sandwich = sandwiches.read_one(db, sandwich_id=sandwich_id)
    if sandwich is None:
        raise HTTPException(status_code=404, detail="User not found")
    return sandwich

@app.put("/sandwiches/{sandwich_id}", response_model=schemas.Sandwich, tags=["Sandwiches"])
def update_one_sandwich(sandwich_id: int, sandwich: schemas.SandwichUpdate, db: Session = Depends(get_db)):
    sandwich_db = sandwiches.read_one(db, sandwich_id=sandwich_id)
    if sandwich_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return sandwiches.update(db=db, sandwich=sandwich, sandwich_id=sandwich_id)

@app.delete("/sandwiches/{sandwich_id}", tags=["Sandwiches"])
def delete_one_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    sandwich = orders.read_one(db, order_id=sandwich_id)
    if sandwich is None:
        raise HTTPException(status_code=404, detail="User not found")
    return sandwiches.delete(db=db, sandwich_id=sandwich_id)






# Promotion CRUD
@app.post("/promotions/", response_model=schemas.Promotion, tags=["Promotions"])
def create_promotion(promotion: schemas.PromotionCreate, db: Session = Depends(get_db)):
    return promotions.create(db=db, promotion=promotion)

@app.get("/promotions/", response_model=list[schemas.Promotion], tags=["Promotions"])
def read_promotions(db: Session = Depends(get_db)):
    return promotions.read_all(db)

@app.get("/promotions/{promotion_id}", response_model=schemas.Promotion, tags=["Promotions"])
def read_one_promotion(promotion_id: int, db: Session = Depends(get_db)):
    promotion = promotions.read_one(db, promotion_id=promotion_id)
    if promotion is None:
        raise HTTPException(status_code=404, detail="User not found")
    return promotion

@app.put("/promotions/{promotion_id}", response_model=schemas.Promotion, tags=["Promotions"])
def update_one_promotion(promotion_id: int, promotion: schemas.PromotionUpdate, db: Session = Depends(get_db)):
    promotion_db = promotions.read_one(db, promotion_id=promotion_id)
    if promotion_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return promotions.update(db=db, promotion=promotion, promotion_id=promotion_id)

@app.delete("/promotions/{promotion_id}", tags=["Promotions"])
def delete_one_promotion(promotion_id: int, db: Session = Depends(get_db)):
    promotion = promotions.read_one(db, promotion_id=promotion_id)
    if promotion is None:
        raise HTTPException(status_code=404, detail="User not found")
    return promotions.delete(db=db, promotion_id=promotion_id)







# Feedback CRUD
@app.post("/feedbacks/", response_model=schemas.Feedback, tags=["Feedbacks"])
def create_feedback(feedback: schemas.FeedbackCreate, db: Session = Depends(get_db)):
    return feedbacks.create(db=db, feedback=feedback)

@app.get("/feedbacks/", response_model=list[schemas.Feedback], tags=["Feedbacks"])
def read_feedbacks(db: Session = Depends(get_db)):
    return feedbacks.read_all(db)

@app.get("/feedbacks/{feedback_id}", response_model=schemas.Feedback, tags=["Feedbacks"])
def read_one_feedback(feedback_id: int, db: Session = Depends(get_db)):
    feedback = feedbacks.read_one(db, feedback_id=feedback_id)
    if feedback is None:
        raise HTTPException(status_code=404, detail="User not found")
    return feedback

@app.put("/feedbacks/{feedback_id}", response_model=schemas.Feedback, tags=["Feedbacks"])
def update_one_feedback(feedback_id: int, feedback: schemas.FeedbackUpdate, db: Session = Depends(get_db)):
    feedback_db = feedbacks.read_one(db, feedback_id=feedback_id)
    if feedback_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return feedbacks.update(db=db, feedback=feedback, feedback_id=feedback_id)

@app.delete("/feedbacks/{feedback_id}", tags=["Feedbacks"])
def delete_one_feedback(feedback_id: int, db: Session = Depends(get_db)):
    feedback = feedbacks.read_one(db, feedback_id=feedback_id)
    if feedback is None:
        raise HTTPException(status_code=404, detail="User not found")
    return feedbacks.delete(db=db, feedback_id=feedback_id)
