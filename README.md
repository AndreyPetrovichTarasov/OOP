# Проект "Приложение для интернет магазина"

## Описание:
Скоро здесь появится подробное описание проекта


## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/username/myblog.git
```

2. Установите зависимостей:
```
pip install -r requirements.txt
```
## Функционал программы
Реализована функция new_product, с помощью которой можно добавлять новые товары.
С помощью функции add_product можно добавлять товары в список категории.
Для класса Product атрибут цены приватный.
В сеттере реализована проверка: в случае если цена равна или ниже нуля, выводится сообщение в консоль 
“Цена не должна быть нулевая или отрицательная”

В программе реализовано строковое представление товаров и категорий.
Есть функциональность сложение товаров.

## Использование:
Для запуска программы запустите файл main.py

## Тестирование:

Для запуска текстов необходимо установить библиотеку pytest.
pip install pytest
poetry add --group dev pytest

Для остлеживания процента покрытия кода тестами, 
дополнительно установить pytest -cov.

После установки pytest можно запустить тесты, выполнив следующую команду:
pytest tests/.

Убедитесь, что все тесты проходят успешно перед внесением изменений в код.

## Логирование

В приложениее будет реализовано логирование событий.
Лог-файлы будут записываться в папку logs.

## Документация:

Дополнительная информация об этом проекте в разработке.

## Лицензия:

Проект распространяется под [лицензией MIT](LICENSE).
