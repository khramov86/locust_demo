## Locust notes from different courses and videos


### Описание
Основные сущности в locust

Locust - Один экземпляр саранчи из роя, налетающий на ваш сервер и мучающий его,

жвиет в gevent гринлете

TaskSet - "мозг" саранчи, набор из функций (классов) Python, которые выполняют работу

по симуляции нагрузки на сервер

##### Чтобы использовать скрипт

`pip install locust`

### Выполнение простого теста

выполнить:

`locust -f http_ping.py --host http://target_hostname:80`

зайти на:

http://localhost:8089/

Для работы из консоли
```
locust -f http_ping.py --host http://targethost:80 --no-web -c 100 -r 100 -n 5000
```
### Описание подготовки веб-сервера
```
https://github.com/khramov86/locust_demo/blob/master/DEPLOY.md
```
Тестирование сервера
```
locust -f http_simulate_news_app.py --host http://docker:84
locust -f http_simulate_news_app.py --host http://docker:84  --no-web -c 100 -r 100 -n 5000
```




## Some links
```
https://docs.locust.io/en/stable/writing-a-locustfile.html

https://github.com/drednout/locust_on_meetup
```
## Material used
https://www.youtube.com/watch?v=65Xa__DMhAw
 
