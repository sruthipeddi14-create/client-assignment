from jsonschema import ValidationError, validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_

'''
TODO: Finish this test by...
1) Troubleshooting and fixing the test failure
The purpose of this test is to validate the response matches the expected schema defined in schemas.py
'''
def test_pet_schema():
    test_endpoint = "/pets/1"

    response = api_helpers.get_api_data(test_endpoint)

    assert response.status_code == 200
    

    # Validate the response schema against the defined schema in schemas.py
    try:
        validate(instance=response.json(), schema=schemas.pet)
    except ValidationError as e:
        pytest.fail(f"Schema invalid: {e}")

'''
TODO: Finish this test by...
1) Extending the parameterization to include all available statuses
2) Validate the appropriate response code
3) Validate the 'status' property in the response is equal to the expected status
4) Validate the schema for each object in the response
'''
@pytest.mark.parametrize("status", [("available")])
def test_find_by_status_200(status):
    test_endpoint = "/pets/findByStatus"
    params = {
        "status": status
    }

    response = api_helpers.get_api_data(test_endpoint, params)
    assert response.status_code == 200
    response_data = response.json()
    try:
        validate(instance=response_data, schema={"type": "array", "items": schemas.pet})
    except ValidationError as e:
        pytest.fail(f"Schema invalid: {e}") 

'''
TODO: Finish this test by...
1) Testing and validating the appropriate 404 response for /pets/{pet_id}
2) Parameterizing the test for any edge cases
'''
def test_get_by_id_404():
    response = api_helpers.get_api_data("/pets/999999")
    assert response.status_code == 404  