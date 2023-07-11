# Image loader 
This project is written in asynchronous FastAPI and aiogram, through which users can collect their images

## Installation

Python or Docker must be already installed

```shell
git clone https://github.com/manjustice/image_loader.git
cd image_loader
Copy .env.sample -> .env and populate with all required data
```

If you have docker you can use this:
```shell
sudo docker run -d -p 8000:8000 -p 443:443 -t $(sudo docker build -q .) (on Linux/macOS)
docker run -d -p 8000:8000 -p 443:443 -t $(docker build -q .) (on Windows)
```

If you don't have it follow this commands:
```shell
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on Linux/macOS)
pip install -r requirements.txt
alembic upgrade head 
uvicorn main:app --host 127.0.0.1 --port 8000 (start it in first terminal)
python bot.py (start it in second terminal)
```

## Usage

To check which user uploaded the images, follow this link:
http://127.0.0.1:8000/

