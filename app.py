from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head><title>CI/CD Pipeline</title></head>
    <body style="font-family:Arial;text-align:center;padding:60px;background:#f0f4f8">
    <h1 style="color:#1F4E79">CI/CD Pipeline - Live on AWS</h1>
    <p>Automatically deployed using GitHub Actions + Docker + AWS EC2</p>
    <p>Built by Vamshi Kanagandla</p>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
