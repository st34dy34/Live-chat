# Live Chat Project

This is a real-time web chat application built using Django Channels and Daphne. It demonstrates that it's possible to implement WebSocket communication in Django to enable instant messaging between users without page reloads.

---
<img src="https://i.imgur.com/k6JdNum.png" alt="My Image" width="500" />




## ⚙️ Requirements

- Python 3.10+  
- Virtualenv (strongly recommended)  
- Windows (tested) / Linux (should work similarly)  
- Git (optional, for cloning repo)

---

## 🛠️ Setup & Installation

```bash
# Clone repo (or download ZIP)
git clone https://github.com/yourusername/live-chat.git
cd live-chat

# Create & activate virtual environment
python -m venv venv
venv\Scripts\activate.bat     # Windows
# source venv/bin/activate    # Linux/macOS

# Install dependencies
pip install -r requirements.txt

# Apply DB migrations
python manage.py migrate
```
## 🚀 Running the server

### Use the provided launcher script:

```bash
start_server.bat
```
You’ll see a clean message like:
```bash
==============================================
  Starting Daphne server on http://0.0.0.0:8000 ...
==============================================
```


