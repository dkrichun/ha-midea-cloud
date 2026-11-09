"""Diagnostics for Daichi integration.

Кнопка "Скачать диагностику" (Настройки -> Устройства и службы -> Daichi -> ⋮)
отдаст JSON со всеми данными устройств, которые вернуло облако:
полный список функций, их состояния, диапазоны значений и т. д.
"""
from __future__ import annotations

from typing import Any

from homeassistant.components.diagnostics import async_redact_data
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

# Подправьте под реальные имена полей, если в дампе остались личные данные
TO_REDACT = {
    "password",
    "token",
    "access_token",
    "refresh_token",
    "username",
    "login",
    "email",
    "phone",
    "mac",
    "serial",
    "address",
}


async def async_get_config_entry_diagnostics(
    hass: HomeAssistant, entry: ConfigEntry
) -> dict[str, Any]:
    """Return diagnostics for a config entry."""
    coordinator = entry.runtime_data
    return {
        "entry": async_redact_data(dict(entry.data), TO_REDACT),
        "devices": async_redact_data(coordinator.data or {}, TO_REDACT),
    }
