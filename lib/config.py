class Config:
    def __init__(self, user, password, host, port, database):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database


cfg = Config(
    user='bn_opencart',
    password='',
    host='172.18.0.3',
    port=3306,
    database='bitnami_opencart'
)
