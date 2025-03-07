SECRET_KEY = 'jogoteca'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = '046733',
        servidor = 'localhost',
        database = 'jogoteca'
    )