import json

from custom_components.loxone import build_minimal_event_payload, extract_uuid_updates


def test_extract_uuid_updates_single_payload():
    uuid_value = "123e4567-e89b-12d3-a456-426614174000"
    message = {"uuid": uuid_value, "value": 42}
    assert extract_uuid_updates(message) == {uuid_value: 42}


def test_extract_uuid_updates_from_map():
    uuid_value = "123e4567-e89b-12d3-a456-426614174000"
    message = {
        uuid_value: 1,
        "control": "/foo",
        "value": "bar",
    }
    assert extract_uuid_updates(message) == {uuid_value: 1}


def test_build_minimal_event_payload_truncates_large_values():
    uuid_value = "123e4567-e89b-12d3-a456-426614174000"
    value = "x" * 40000
    payload = build_minimal_event_payload(uuid_value, value)
    assert payload["uuid"] == uuid_value
    assert payload.get("truncated") is True
    assert len(json.dumps(payload, default=str)) < 30000
