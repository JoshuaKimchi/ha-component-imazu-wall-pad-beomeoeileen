"""Button platform for Imazu Wall Pad integration."""
import logging
from homeassistant.components.button import ButtonEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

# gateway와 config entry 타입을 정확히 명시하기 위해 import 합니다.
from . import ImazuGateway, ImazuWallPadConfigEntry

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ImazuWallPadConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Initialize Imazu Wall Pad button platform."""
    # 지금은 아무런 엔티티도 추가하지 않고, 함수가 정상적으로 실행되는지만 확인합니다.
    _LOGGER.info("Imazu Wall Pad button platform setup successfully.")
    
    # 빈 리스트를 전달하여 아무것도 추가하지 않음
    async_add_entities([])

# 클래스 정의만 해두고, 실제 인스턴스는 만들지 않습니다.
class WPElevatorCallButton(ButtonEntity):
    """Placeholder for a Wall Pad elevator call button."""
    pass
