﻿# Blackpoint
Телеграм-приложение для покупки кофе в автоматах по qr-коду и подписке

# Описание
Пользователь может оформить подписку на ежедневное кол-во чашек кофе в выбранном им автомате.
Автомат можно выбрать на карте или отсканировав qr-код, расположенный на автомате.
Подписка позволяет получить напиток в автомате, выбрав позицию в приложении. 
Приложение использует api эквайринг системы Vendista и сервис Paykeeper для приёма платежей

# Установка и запуск
```bash
git clone https://github.com/yavorich/blackpoint.git
cd project
make up
```
# Применение миграций
```bash
make migrate
```
