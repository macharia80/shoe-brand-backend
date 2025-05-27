# models.py
from sqlalchemy import Column, Integer, String, Float
from database import Base

class Shoe(Base):
    __tablename__ = 'shoes'

    id = Column(Integer, primary_key=True)
    brand = Column(String(100), nullable=False)
    model = Column(String(100), nullable=False)
    size = Column(Float, nullable=False)
    price = Column(Float, nullable=False)

    def __repr__(self):
        return f"<Shoe(id={self.id}, brand='{self.brand}', model='{self.model}', size={self.size}, price={self.price})>"