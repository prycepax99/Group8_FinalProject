from fastapi.testclient import TestClient
from ..controllers import orders, order_details, resources, sandwiches, recipes
from ..main import app
import pytest
from ..models import models

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_order(db_session):
    # Create a sample order
    order_data = {
        "customer_name": "John Doe",
        "description": "Test order"
    }

    order_object = models.Order(**order_data)

    # Call the create function
    created_order = orders.create(db_session, order_object)

    # Assertions
    assert created_order is not None
    assert created_order.customer_name == "John Doe"
    assert created_order.description == "Test order"

def test_create_order_details(db_session):
    # Create a sample order
    order_detail_data = {
        "order_id": "John Doe",
        "sandwich_id": "Test item",
        "amount": 2
    }

    order_detail_object = models.OrderDetail(**order_detail_data)

    # Call the create function
    created_order_detail = order_details.create(db_session, order_detail_object)

    # Create a sample order details
    order_details_data = {
        "order_id": created_order_detail.id,
        "sandwich_id": "Test item",
        "amount": 2
    }

    order_details_object = models.OrderDetail(**order_details_data)

    # Call the create function
    created_order_details = order_details.create(db_session, order_details_object)

    # Assertions
    assert created_order_details is not None
    assert created_order_details.order_id == created_order_details.id
    assert created_order_details.sandwich_id == "Test item"
    assert created_order_details.amount == 2

def test_create_resource(db_session):
    # Create a sample resource
    resource_data = {
        "item": "Test item",
        "amount": 2
    }

    resource_object = models.Resource(**resource_data)

    # Call the create function
    created_resource = resources.create(db_session, resource_object)

    # Assertions
    assert created_resource is not None
    assert created_resource.item == "Test item"
    assert created_resource.amount == 2

def test_create_sandwich(db_session):
    # Create a sample sandwich
    sandwich_data = {
        "sandwich_name": "Test sandwich",
        "price": 5.99
    }

    sandwich_object = models.Sandwich(**sandwich_data)

    # Call the create function
    created_sandwich = sandwiches.create(db_session, sandwich_object)

    # Assertions
    assert created_sandwich is not None
    assert created_sandwich.sandwich_name == "Test sandwich"
    assert created_sandwich.price == 5.99

# def test_create_recipe(db_session):
#     # Create a sample sandwich
#     recipe_data = {
#         "sandwich_id": "Test sandwich",
#         "resource_id": 2,
#         "amount": 2
#     }
#
#     recipe_object = models.Sandwich(**recipe_data)
#
#     # Call the create function
#     created_recipe = recipes.create(db_session, recipe_object)
#
#     # Create a sample resource
#     recipe_data = {
#         "sandwich_id": "Test sandwich",
#         "resource_id": 2,
#         "amount": 2
#     }
#
#     resource_object = models.Resource(**recipe_data)
#
#     # Call the create function
#     created_recipe = recipes.create(db_session, resource_object)
#
#     # Create a sample recipe
#     recipe_data = {
#         "sandwich_id": created_recipe.sandwich_id,
#         "resource_id": created_recipe.resource_id,
#         "amount": 2
#     }
#
#     recipe_object = models.Recipe(**recipe_data)
#
#     # Call the create function
#     created_recipe = recipes.create(db_session, recipe_object)
#
#     # Assertions
#     assert created_recipe is not None
#     assert created_recipe.sandwich_id == created_recipe.sandwich_id
#     assert created_recipe.resource_id == created_recipe.sandwich_id
#     assert created_recipe.amount == 2