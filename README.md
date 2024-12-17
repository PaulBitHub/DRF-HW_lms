# LMS-система 

LMS-система - это веб-приложение, позволяющее пользователям размещать свои полезные материалы и курсы.

## Описание

LMS-система позволяет создавать и управлять курсами, добавлять материалы, а также предоставляет функционал для управления пользователями и их доступами.

## Требования к проекту

* Python: версия 3.8 или выше
* Django: версия 3.2 или выше
* PostgreSQL: версия 12 или выше


## Installation and Setup

### 1. Clone the Repository

```bash
git clone git@github.com:PaulBitHub/DRF-HW_lms
cd DRF-HW_lms
```
### 2. Copy the env.example file to .env:

Open.env and replace the values of the variables with your own

```bash
cp .env.example .env
```

### 3. Install Dependencies
The project uses Pip for dependency management. Ensure Pip is installed, then run the following command to install all dependencies:
```bash
pip install -r requirements.txt
```
### 4. Start Migrations
To start migrations, use the following command:
```bash
python3 manage.py migrate
```

### 5. Create Superuser
Enter the command in the terminal:
```bash
python3 manage.py create_superuser
```

### 6. Load Fixture
Loading test fixtures for the database:
```bash
python3 manage.py loaddata data.json
```

### 7. Create Group
Loading test fixtures for the database:
```bash
python3 manage.py create_groupe
```


### 8. Create Manager and Content-Manager
Enter the command in the terminal:
```bash
python3 manage.py create_staff
```


### 9. Run Server
To run server, use the following command:
```bash
python3 manage.py runserver
```
The server will be available at http://127.0.0.1:8000

## Дополнительная информация для проверяющего
1. Пункт 5 (Create Superuser) создаст суперпользователя
    * email: admin@test.com
    * password: 12345678
2. Пункт 6 (Load Fixture) выполнит загрузку в БД:
   * 5 статей для блога
   * 3 клиентов (владелец superuser)
   * 3 сообщений для рассылки (владелец superuser)
   * 3 рассылки (владелец superuser)
3. Пункт 7 (Create Group) создаст:
   * regular_user - новые зарегестрированные пользователи платформы, имеют доступ только к своим созданным клиентам, сообщениям, рассылкам
   * manager - пользователи имеют только ограниченный доступ к странице рассылки (просмотр списка, детальный просмотр, деактивация), пользователей (просмотр списка, деактивация)
   * content-manager - пользователи имеют доступ только к административной панели модели статей
   * superuser имеет доступ и права ко всей информации приложения
   * К страницам Главная, Блог, имеют доступ все неавторизованные пользователи

4. Пункт 8 (Create Manager and Content-Manager) создаст пользователей, добавит в соответствующие группы (manager, content_manager)
    * email: manager@test.com
    * email: content_manager@test.com
    * password: 12345678
5. Отправка запланированной рассылки осуществляется через интерфейс сайта
6. Мгновенная отправка осуществляется командой
    ```bash
    python3 manage.py send_mail
    ```
   При выполнении команды следуйте инструкции выбора рассылки. При выполнении мгновенной рассылки попытка рассылки сохранется в БД, время следующей отправки не изменяется

