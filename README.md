# Sign Language Translator
Our project for Unihack 2020.
Translate sign language to text
Currently only supports ASL

## Setting up
Clone the repository
```sh
git clone https://github.com/lestherll/sign_lang_translator.git
```

Navigate directory
```sh
cd sign_lang_tanslator
```

Configuring virtual environment
```py
python3 -m venv venv
```

Installing dependencies
```sh
pip install -r requirements.txt
```

## Usage
For Linux and Mac:
```sh
export FLASK_APP=sign_lang_translator
export FLASK_ENV=development
flask run
```

For Windows cmd, use set instead of export:
```sh
set FLASK_APP=sign_lang_translator
set FLASK_ENV=development
flask run
```

For Windows PowerShell, use $env: instead of export:
```sh
$env:FLASK_APP = "sign_lang_translator"
$env:FLASK_ENV = "development"
flask run
```