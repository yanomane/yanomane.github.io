from flask import Flask

app = Flask(__name__)


@app.route('/')
def alo_mundo():
    return 'Aló Mundo , Seja bem Vindo!'

if __name__ == '__main__':
    app.run()


