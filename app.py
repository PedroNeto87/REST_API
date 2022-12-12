from flask import Flask

app = Flask(__name__)

stores = [
    {
        'name': 'My Store',
        'items': [
            {'name': 'Chair', 
            'price': 15.99},
            {'name': 'Book',
            'price': 10.99}
        ]
    }
]

@app.get('/store') #Endpoint
def get_stores():
    return{'stores': stores}
