from bluelog import create_app  # noqa

# app = create_app('production')
app = create_app('development')

# 开发时的程序入口

if __name__ == '__main__':
    app.run(debug=True, port=5000)
