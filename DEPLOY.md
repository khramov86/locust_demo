###Деплоймент приложения


##
####На веб-сервер (Ubuntu)
sudo apt-get install nginx-full apache2-utils

git clone https://github.com/drednout/locust_on_meetup

cd locust_on_meetup

cp conf/locust_test /etc/nginx/sites-available/

ln -s /etc/nginx/sites-available/locust_test /etc/nginx/sites-enabled/

htpasswd -c /etc/nginx/.htpasswd test

service nginx reload

если не работает - удалить дефолтный конфиг

rm /etc/nginx/sites-enabled/default
 
##
####Деплоймент в докер
docker run -it -p 82:80 ubuntu

docker exec -it 75645176a880 /bin/bash
####Подготовка контейнера
in container

apt update

apt-get install nginx-full apache2-utils

/etc/init.d/nginx restart
######Проверить nginx
http://hostname_of_dockerhost:port_mapped/


внутри контейнера добавить

cd locust_on_meetup/

cp conf/locust_test /etc/nginx/sites-available/

ln -s /etc/nginx/sites-available/locust_test /etc/nginx/sites-enabled/

htpasswd -c /etc/nginx/.htpasswd test

В контейнере задал пароль test

service nginx reload

rm /etc/nginx/sites-enabled/default

service nginx reload

Проверить внутри контейнера

curl --user test:test -v -XGET http://localhost:80/news
##Контейнер в docker hub
Выйти из конейнера

В общем виде команды
docker commit container_id
docker tag local-image:tagname new-repo:tagname
docker push new-repo:tagname

Если машина не была авторизована на docker-hub, то
docker login
docker push khramov86/locusttest:tagname


 