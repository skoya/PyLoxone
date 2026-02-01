from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from homeassistant.core import HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_send

SIGNAL_UUID_UPDATE = "loxone_uuid_update_{uuid}"


@dataclass
class LoxoneStateCache:
    hass: HomeAssistant
    values: dict[str, Any] = field(default_factory=dict)

    def set(self, uuid: str, value: Any) -> None:
        self.values[uuid] = value

    def get(self, uuid: str) -> Any | None:
        return self.values.get(uuid)

    def has(self, uuid: str) -> bool:
        return uuid in self.values

    def notify(self, uuid: str) -> None:
        async_dispatcher_send(self.hass, SIGNAL_UUID_UPDATE.format(uuid=uuid))
