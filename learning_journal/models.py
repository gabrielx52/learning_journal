from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    func,

    )

from datetime import datetime


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
    )

from zope.sqlalchemy import ZopeTransactionExtension


DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

def time_str(time_obj):
    time_str = str(datetime.now)
    return time_str()

class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)

Index('my_index', MyModel.name, unique=True, mysql_length=255)


class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(CHAR(255), unique=True) # unicode supports char length
    body = Column(Text)
    created = Column(DATETIME(timezone=True), default=func.now())
    edited = Column(DATETIME(timezone=True),default=func.now(), onupdate=func.now())


    # def __init__(self, id, title, body, created, edited):
    #     self.id = id
    #     self.title = title
    #     self.body = body
    #     self.created = 'nuts'
    #     self.edited = timezone('US/Pacific').localize(edited)


    # @validates('title')
    # def validate_title(self, key, title):
    #     assert len(title) <= 255, 'Title must be less than 255 characters'
    #     return title


    # @classmethod
    # def all(cls):
    #     pass
    #
    # @classmethod
    # def by_id(cls, id):
    #     return Session.query(id).filter(id=id)

Index('Entry_Index', Entry.title, unique=True, mysql_length=255)


