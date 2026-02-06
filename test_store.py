from tkinter.messagebox import IGNORE
from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_

'''

TODO: Finish this test by...
1) Creating a function to test the PATCH request /store/order/{order_id}
2) *Optional* Consider using @pytest.fixture to create unique test data for each run
2) *Optional* Consider creating an 'Order' model in schemas.py and validating it in the test
3) Validate the response codes and values
4) Validate the response message "Order and pet status updated successfully"
'''

def unique_order_data():
    return {
        "id": 123456,
        "petId": 1,
        "quantity": 1,
        "shipDate": "2024-01-01T00:00:00.000Z",
        "status": "placed",
        "complete": False
    }

def test_patch_order_by_id(unique_order_data):
    # First, create a new order to ensure it exists
    create_response = api_helpers.post_api_data("/store/order", unique_order_data)
    assert create_response.status_code == 200

    order_id = unique_order_data["id"]
    patch_data = {
        "status": "delivered",
        "complete": True
    }

    # Now, send the PATCH request to update the order
    patch_response = api_helpers.patch_api_data(f"/store/order/{order_id}", patch_data)
    assert patch_response.status_code == 200

    response_json = patch_response.json()
    assert_that(response_json['status'], is_("delivered"))
    assert_that(response_json['complete'], is_(True))
    assert_that(response_json['message'], contains_string("Order and pet status updated successfully"))