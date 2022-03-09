from my_app import create_app, config

app = create_app(config.DevelopmentConfig)


@app.route('/')
def hello_world():
    return 'Hello World 1!'


if __name__ == '__main__':
    app.run()
