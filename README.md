# Онлайн платформа-торговой сети электроники "Techno_logic"
---

## Описание
**"Techno_logic"** — Онлайн платформа-торговой сети.

## Технологии, использованные в проекте
- **Backend:** Python, Django
- **Frontend:** HTML, CSS (и другие технологии, если используются)
- **База данных:** PostgreSQL (по умолчанию, или другая, если используется)

---

# Инструкция

## Локальное использование

### Установка
1. **Клонировать репозиторий:**
   - `git clone https://github.com/PaulBitHub/electronic_network_project.git`
   - Перейти в папку с проектом (пример: `cd electronic_network_project`)

2. **Активировать виртуальное окружение:**
   - `poetry shell`

3. **Установите зависимости:**
   - `poetry install`

---

### Настройка

1. **Создайте файл `.env` с переменными окружения:** (можно опустить для данного задания)
   - На основе файла `.env.sample`.

2. **Примените миграции:**
   - `python manage.py migrate`.

3. **Создание суперпользователя:**
   - используйте команду `python manage.py createsuperuser`.
   или
   - Отредактируйте файл `users/management/commands/csu.py`.
   - Создайте пользователя командой: `python manage.py csu`.

### Запуск
1. **Запустите сервер:**
   - `python manage.py runserver`
   - Приложение будет доступно по адресу: [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
