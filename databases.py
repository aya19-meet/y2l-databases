from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()



def create_product(name, price, quantity, description, malaks_approval, recommendation):
	product_object = Product(
		name=name,
		price=price,
		quantity=quantity,
		description=description,
		malaks_approval=malaks_approval,
		recommendation=recommendation)
	session.add(product_object)
	session.commit()
def update_product(name, quantity, price):
	product_object = session.query(
		Product).filter_by(
		name=name).first()
	product_object.quantity = quantity
	product_object.price = price
	session.commit()
def delete_product(name):
	session.query(Product).filter_by(
		name=name).delete()
	session.commit()


def get_product(id):
  pass

# create_product("table",10,20,"nice comfortable for legged table", True, "very good")
# delete_product("table")
# create_product("chair",40,50,"black nice chair",False,"great")