from api import db
from sqlalchemy import Column, Integer, String, Boolean, DateTime

class Processes(db.Model):
    id = Column(Integer, primary_key=True)
    ref_number = Column(Integer)
    input_filename = Column(String(100))
    output_filename = Column(String(100))
    start_time = Column(DateTime)
    input_filepath = Column(String(200))
    status = Column(String(20))

    def __init__(self, status):
        self.status = status

    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
