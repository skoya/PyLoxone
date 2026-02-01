from unittest.mock import MagicMock, patch

from custom_components.loxone.state_cache import LoxoneStateCache, SIGNAL_UUID_UPDATE


def test_state_cache_set_get_has():
    hass = MagicMock()
    cache = LoxoneStateCache(hass)
    cache.set("uuid-1", 123)
    assert cache.has("uuid-1") is True
    assert cache.get("uuid-1") == 123


def test_state_cache_notify_dispatches_signal():
    hass = MagicMock()
    cache = LoxoneStateCache(hass)
    with patch("custom_components.loxone.state_cache.async_dispatcher_send") as send:
        cache.notify("uuid-2")
        send.assert_called_once_with(hass, SIGNAL_UUID_UPDATE.format(uuid="uuid-2"))
