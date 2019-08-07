from model import Base, Store

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///stores.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_store(name, phone, city, street):
    """Add a store to the DB."""
    store = Store(name=name, phone=phone, city=city, street=street)
    session.add(store)
    session.commit()

def query_all():
	print('b')
	return session.query(Store).all()

def get_store(name):
    """Find the first store in the DB, by thr name."""
    return session.query(Store).filter_by(name=name).first()

def guery_by_city(city):
	return session.query(Store).filter_by(city=city).all()
	pass

def remove_store(name):
    session.query(Store).filter_by(name=name).first().remove()
    session.commit()