from unittest.mock import patch

import pytest

from src.main import create_incident


@patch("src.main.os.getenv")
@patch("requests.post")
def test_create_incident_success(mock_post, mock_getenv):
    mock_getenv.side_effect = lambda k: {
        "SNOW_INSTANCE": "https://fake.service-now.com",
        "SNOW_USER": "admin",
        "SNOW_PASS": "pass",
    }[k]

    mock_post.return_value.status_code = 201
    mock_post.return_value.json.return_value = {"result": {"number": "INC0012345"}}

    create_incident("CLI Test", "Test incident from CLI")

    mock_post.assert_called_once()
    args, kwargs = mock_post.call_args
    assert args[0] == "https://fake.service-now.com/api/now/table/incident"
    assert kwargs["headers"]["Content-Type"] == "application/json"
    assert kwargs["json"]["short_description"] == "CLI Test"


@patch("requests.post")
def test_create_incident_failure(mock_post):
    mock_post.return_value.status_code = 401
    mock_post.return_value.text = "Unauthorized"

    create_incident("Fail Test", "Expecting failure")


def test_create_incident_raises_type_error_if_description_is_not_string():
    with pytest.raises(TypeError):
        create_incident(123, "Expecting failure")
    with pytest.raises(TypeError):
        create_incident("Fail Test", 123)


def test_create_incident_raises_value_error_if_description_is_empty():
    with pytest.raises(ValueError):
        create_incident("", "Expecting failure")
    with pytest.raises(ValueError):
        create_incident("Fail Test", "")


def test_create_incident_raises_value_error_if_description_are_digits():
    with pytest.raises(ValueError):
        create_incident("123", "Expecting failure")
    with pytest.raises(ValueError):
        create_incident("Fail Test", "123")


def test_create_incident_raises_value_error_if_description_contains_invalid_characters():
    with pytest.raises(ValueError):
        create_incident("ERROR!", "Expecting failure")
    with pytest.raises(ValueError):
        create_incident("Fail Test", "Test!")
