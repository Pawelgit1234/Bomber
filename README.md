# Bomber
## What can do this bomber
- Email DOS attacks
- Email DDOS attacks
- Send HTML
- Send PDF

## Install
```bash
git clone https://github.com/Pawelgit1234/Bomber.git
```
### Create .env
```text
SENDER_EMAIL="<your sender email>"
SENDER_EMAIL_PASSWORD="<your sender email password>"
RECEIVER_EMAIL="<your email getter>"
```

### Create DDOS.json
```json
{
  "emails": [
    [
      "<sender email>",
      "<sender email password>"
    ],
    [
      "<another sender email>",
      "<another sender email password>"
    ]
  ]
}
```
### Install requirements.txt
````commandline
pip install -r requirements.txt
````

## Run
````commandline
python main.py
````