"""Button platform for Imazu Wall Pad integration."""
import logging
from homeassistant.components.button import ButtonEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from . import ImazuGateway, ImazuWallPadConfigEntry
from .const import BRAND_NAME, DOMAIN, MANUFACTURER, MODEL

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ImazuWallPadConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Initialize Imazu Wall Pad button platform."""
    gateway: ImazuGateway = entry.runtime_data
    
    # 이제 실제로 엔티티를 추가합니다.
    async_add_entities([WPElevatorCallButton(gateway)])
    
    _LOGGER.info("Imazu Wall Pad elevator button has been added.")


class WPElevatorCallButton(ButtonEntity):
    """Representation of a Wall Pad elevator call button."""

    def __init__(self, gateway: ImazuGateway) -> None:
        """Initialize the button."""
        self._gateway = gateway
        self._attr_name = f"{BRAND_NAME} Elevator Call".title()
        self._attr_unique_id = f"{DOMAIN}-{self._gateway.host}-elevator-call"
        self._attr_icon = "mdi:elevator-passenger"

    @property
    def available(self) -> bool:
        """Return True if the gateway is connected."""
        return self._gateway.connected

    async def async_press(self) -> None:
        """Handle the button press event."""
        _LOGGER.info("Elevator call button pressed. Calling gateway function.")
        # 이 함수는 나중에 gateway.py에 추가할 것입니다.
        # 지금은 호출하는 부분만 만들어 둡니다.
        await self._gateway.call_elevator()

    @property
    def device_info(self):
        """Return device information to group entities under a single device."""
        return {
            "identifiers": {(DOMAIN, self._gateway.host, "elevator")},
            "name": f"{BRAND_NAME} Elevator",
            "manufacturer": MANUFACTURER,
            "model": MODEL,
        }
