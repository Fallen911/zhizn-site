# zhizn-site

Статический сайт приложения SurnovLifeManager («Жизнь»): страница поддержки и политика конфиденциальности. URL политики указан в App Store Connect, поэтому пути `index.html` и `privacy.html` менять нельзя.

- Стек: чистый HTML + встроенный CSS, без сборки и зависимостей.
- Деплой: GitHub Pages из ветки `main` → https://fallen911.github.io/zhizn-site/
- Локально: `python3 -m http.server 8000` и открыть http://localhost:8000
- Переменных окружения нет.

Политика должна совпадать с тем, что реально собирает приложение (репозиторий life-manager: Supabase, PowerSync, Google Calendar, Telegram). При изменении — обновить дату в обеих языковых версиях.
