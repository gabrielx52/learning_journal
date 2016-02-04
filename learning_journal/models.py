from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime,
    func,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension


DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()



class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)

Index('my_index', MyModel.name, unique=True, mysql_length=255)


class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Text, mysql_length=255, unique=True) # need to figure out how to limit length properly
    body = Column(Text)
    created = Column(DateTime(timezone=True), default=func.now())
    edited = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())

Index('Entry_Index', Entry.title, unique=True, mysql_length=255)

    # def all(self):
    #     pass
    #
    # def by_id(self):
    #     pass