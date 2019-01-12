from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import connectors
from sqlalchemy import engine
a = engine.Connectable()
a.connect()

metadata = MetaData()

#Creates an engine and db
engine = create_engine('sqlite:///C:\\Users\\user\\sqlAlchemy\\db1.db', echo=True)


users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String),
              Column('fullname', String),
              )

addresses = Table('addresses', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('user_id', None, ForeignKey('users.id')),
                  Column('email_address', String, nullable=False)
                  )



metadata.create_all(engine)
