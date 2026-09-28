[README.md](https://github.com/user-attachments/files/32773176/README.md)# Tic-Tac-Toe — Android APK через GitHub Actions

Готовый проект для сборки debug APK из `main.py`.

## Что исправлено

- Добавлен локальный recipe для `pygame-ce`.
- `buildozer.spec` подключает его через `p4a.local_recipes`.
- Используется `python-for-android` ветки `develop`, где поддерживается текущая схема локальных recipes.
- Workflow сохраняет полный `build.log`, если сборка снова упадёт.
- Готовый APK автоматически загружается как artifact `TicTacToe-APK`.

## Как поставить в GitHub

Замени файлы в репозитории этими файлами, сохранив структуру папок:

```text
.
├── main.py
├── buildozer.spec
├── README.md
├── .gitignore
├── p4a-recipes/
│   └── pygame-ce/
│       └── __init__.py
└── .github/
    └── workflows/
        └── build-apk.yml
```

После push открой **Actions → Build APK**. Workflow можно запустить вручную через **Run workflow**.

## Где APK

После успешной сборки открой завершённый запуск workflow и скачай artifact **TicTacToe-APK**.

## Если сборка снова упадёт

В красном запуске Actions появится artifact **build-log**. Он содержит полный лог, включая строку с настоящей причиной ошибки, а не только финальный `Buildozer failed`.
