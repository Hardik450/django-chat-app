

````markdown
# 💬 Django Chat App

A real-time chat application built using **Django**, **Channels (WebSockets)**, and **MongoDB**, offering user authentication and a responsive UI inspired by messaging apps.

---

## 🚀 Features

- 🔐 User Registration & Login (with Django Auth)
- 🧑‍🤝‍🧑 Real-Time Global Chat using WebSockets (Django Channels)
- 💾 Message persistence using **MongoDB**
- 🖼️ Clean UI with responsive design (inspired by modern messaging apps)
- 📜 Previous messages auto-loaded on page refresh
- 🌐 Deployed with Daphne (ASGI server)

---

## 🛠️ Tech Stack

| Technology        | Usage                             |
|-------------------|-----------------------------------|
| Python / Django   | Web backend, user auth            |
| Django Channels   | Real-time WebSocket communication |
| MongoDB           | Message storage                   |
| HTML, CSS, JS     | Frontend UI                       |
| Daphne            | ASGI deployment                   |



## 🔧 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/hardik450/django-chat-app.git
cd django-chat-app
````

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Linux/Mac
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Configure MongoDB

Set up your MongoDB URI inside `chat/views.py`:

```python
client = MongoClient("YOUR_MONGODB_ATLAS_URI")
```

> 🔐 Use `.env` or Django settings for production!

### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Start ASGI Server (with Daphne)

```bash
daphne chatapp.asgi:application
```

Then go to [http://127.0.0.1:8000/signup/](http://127.0.0.1:8000/signup/) to register and start chatting!

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a PR.

---

## 📜 License

This project is licensed under the **MIT License**. Feel free to use and modify.

---

## 🌟 Author

**Hardik Jain**
🔗 [GitHub](https://github.com/hardik450)

---
