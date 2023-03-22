# Обрезка ссылок с помощью Битли

Данный скрипт предназначен для обрезания (сокращения) длинных ссылок с помощью сервиса Bitly.  
Так же данных скрипт может отображать количество переходов по короткой ссылке.

### Как установить
 
1. Получить `token` сервиса Bitly ([Как получить token](https://dev.bitly.com/docs/getting-started/introduction/))  
2. Присвоить полученный токен переменной окружения `API_TOKEN` 

Python3 должен быть уже установлен.   
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
### Как использовать

Точка входа для работы скрипта файл `main.py`
В качества параметра необходимо указать `url` для сокращения c помощью сервиса Bitly или же url короткой ссылки для получения статистики по количеству переходов по укороченной ссылке.  
 
Например:  
```
python3 main.py https://google.com
Результат >> Битлинк: https://bit.ly/3JTgfT
или
python3 main.py https://bit.ly/FgdGt
Результат >> По вашей ссылке прошли: 15 раз(а)
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).