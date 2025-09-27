"""Constants for the Imazu Wall Pad integration."""

from homeassistant.const import Platform

DOMAIN = "imazu_wall_pad"
BRAND_NAME = "imazu"
MANUFACTURER = "Hyundai HT"
MODEL = "WP-IMAZU"
SW_VERSION = "1.0"

DEFAULT_PORT = 8899

# ▼▼▼▼▼ PLATFORMS 리스트에 SENSOR와 BUTTON을 추가하는 것이 핵심입니다. ▼▼▼▼▼
PLATFORMS = [
    Platform.BINARY_SENSOR,
    Platform.LIGHT,
    Platform.SWITCH,
    Platform.FAN,
    Platform.CLIMATE,
    Platform.SENSOR,
    Platform.BUTTON,
]
# ▲▲▲▲▲ 여기까지 수정 ▲▲▲▲▲

PACKET = "packet"

ATTR_DEVICE = "device"
ATTR_ROOM_ID = "room_id"
ATTR_SUB_ID = "sub_id"

# ▼▼▼▼▼ 엘리베이터 호출 명령어도 미리 추가해 둡니다. ▼▼▼▼▼
PACKET_ELEVATOR_CALL = bytearray([0xF7, 0x0B, 0x01, 0x4B, 0x04, 0x6A, 0x11, 0x00, 0x00, 0xC9, 0xEE])
