##Locust notes from different courses and videos


###Описание
Основные сущности в locust

Locust - Один экземпляр саранчи из роя, налетающий на ваш сервер и мучающий его,
жвиет в gevent гринлете

TaskSet - "мозг" саранчи, набор из функций (классов) Python, которые выполняют работу
по симуляции нагрузки на сервер

#####Чтобы использовать скрипт
pip install locust

###Выполнение простого теста
выполнить:

locust -f http_ping.py --host http://192.168.120.142:80

зайти на:

http://localhost:8089/

Для работы из консоли
locust -f http_ping.py --host http://192.168.120.142:80 --no-web -c 100 -r 100 -n 5000


##Some links
https://docs.locust.io/en/stable/writing-a-locustfile.html

https://github.com/drednout/locust_on_meetup

##Courses used

https://www.youtube.com/watch?v=65Xa__DMhAw
 