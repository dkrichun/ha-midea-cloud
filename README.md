# Daichi Comfort Cloud для Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/hacs/integration)
[![GitHub Release](https://img.shields.io/github/release/dkrichun/ha-midea-cloud.svg?style=flat-square)](https://github.com/dkrichun/ha-midea-cloud/releases/latest)
[![Version](https://img.shields.io/github/v/release/dkrichun/ha-midea-cloud.svg?style=flat-square&label=version&color=blue)](https://github.com/dkrichun/ha-midea-cloud/releases/latest)

Интеграция Home Assistant для управления кондиционерами Midea/Daichi через API Comfort Cloud.
https://web.daichicloud.ru

## ✅ Возможности

- 🌡️ **Управление температурой** (16–30 °C)
- ❄️ **Режимы работы**: охлаждение, обогрев, вентилятор, осушение, авто
- 💨 **Скорость вентилятора**: авто, 1–5
- 🔄 **Предустановленные режимы**: eco, turbo, sleep, comfort sleep
- 🎯 **Режимы качания**: вертикальное, горизонтальное, 3D
- 📊 **Датчики**: температура в помещении, температура на улице, влажность
- 🔄 Автоматическое обновление состояния каждые 60 секунд

## 📦 Установка

### Через HACS (рекомендуется)

1. Убедитесь, что у вас установлен [HACS](https://hacs.xyz/)
2. Перейдите в HACS → Интеграции
3. Нажмите ⋮ → Пользовательские репозитории
4. Добавьте репозиторий:
   - URL: `https://github.com/dkrichun/ha-midea-cloud`
   - Категория: Integration
5. Найдите «Daichi Comfort Cloud» и нажмите «Установить»
6. Перезапустите Home Assistant

### Ручная установка

```bash
# Скопируйте custom_components/midea в ваш Home Assistant
cp -r custom_components/midea /config/custom_components/
```

Перезапустите Home Assistant.

## ⚙️ Настройка

1. Перейдите в **Настройки** → **Устройства и службы**
2. Нажмите **Добавить интеграцию**
3. Найдите **Daichi Comfort Cloud**
4. Введите свои учётные данные:
   - **Email**: адрес электронной почты, используемый для Daichi Comfort Cloud
   - **Пароль**: ваш пароль

## 🎮 Поддерживаемые устройства

Работает со всеми кондиционерами Daichi/Midea, подключёнными к Comfort Cloud:
- Midea Breezeless series
- Другие модели, поддерживаемые Daichi Cloud

## 📋 Поддерживаемые функции

| Функция | Статус |
|---------|--------|
| Включение/выключение | ✅ |
| Установка температуры | ✅ |
| Режим охлаждения | ✅ |
| Режим обогрева | ✅ |
| Режим только вентилятора | ✅ |
| Режим осушения | ✅ |
| Автоматический режим | ✅ |
| Скорость вентилятора (авто, 1–5) | ✅ |
| Режим Eco | ✅ |
| Режим Turbo | ✅ |
| Режим Sleep | ✅ |
| Вертикальное качание | ✅ |
| Горизонтальное качание | ✅ |
| 3D-качание | ✅ |
| Датчик температуры | ✅ |
| Датчик влажности | ✅ |

## 🔧 Отладка

Чтобы включить подробное логирование, добавьте в `configuration.yaml`:

```yaml
logger:
  default: info
  logs:
    custom_components.midea: debug
```

## 📁 Структура проекта

```
custom_components/
  midea/
    __init__.py          # Настройка интеграции
    manifest.json        # Метаданные
    config_flow.py       # Поток настройки через UI
    const.py             # Константы и Function IDs
    api.py               # Клиент API
    coordinator.py       # Координатор обновления данных
    climate.py           # Сущность климата
    sensor.py            # Датчики
    exceptions.py        # Исключения
    translations/        # Переводы
```

## 📖 Документация API

Полный список Function IDs для управления устройством см. в [FUNCTION_IDS.md](https://github.com/dkrichun/ha-midea-cloud/blob/main/FUNCTION_IDS.md).

## 📄 Лицензия

MIT License — см. [LICENSE](https://github.com/dkrichun/ha-midea-cloud/blob/main/LICENSE).

## 🤝 Поддержка

Если возникли проблемы:

1. Включите отладочное логирование
2. Проверьте [Issues](https://github.com/dkrichun/ha-midea-cloud/issues)
3. Создайте новый issue с подробностями и логами
