from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    func,
    MetaData,
    )



from sqlalchemy.dialects.sqlite import (
    CHAR,
    DATETIME,
    )


from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    validates,
    Session,
    query,
    object_session,
    )

from zope.sqlalchemy import ZopeTransactionExtension


DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))


meta = MetaData()


Base = declarative_base(metadata=meta)


sess = Session()

class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)

Index('my_index', MyModel.name, unique=True, mysql_length=255)


class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(CHAR(255), unique=True) # unicode supports char length?
    body = Column(Text)
    created = Column(DATETIME(timezone=True), default=func.now())
    edited = Column(DATETIME(timezone=True),default=func.now(), onupdate=func.now())

    @classmethod
    def by_id(cls, DB, id):
        return DB.query(cls).get(id)


    @classmethod
    def all(cls):
        pass


'''
The entry class should support a classmethod all that returns all the entries in the database,
ordered so that the most recent entry is first.
The entry class should support a classmethod by_id that returns a single entry, given an id.

'''

Index('Entry_Index', Entry.title, unique=True, mysql_length=255)





    # @validates('title')
    # def validate_title(self, key, title):
    #     assert len(title) <= 255, 'Title must be less than 255 characters'
    #     return title

