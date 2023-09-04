from db import db


class Products(db.Model):
    # Define the tablename
    __tablename__ = 'products'

    # Define Columns, (can refer to SQLAlchemy_data_types.py to refering)
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(128))

    @classmethod # Using the cls method to retrieve the products, since we are query to have the product, instead create the blueplan to retrieve the data
    def find_by_id(cls, _id):
        return cls.query.get(_id)
    
    @ckassmethod
    def find_all(cls):
        return cls.query.get_all()

    # while this where cannot using the cls method since the information are manipulating the db, so we creating the session to save or upload the data to db
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


    @property
    def json(self):
        return {
            "id": self.id,
            "name": self.name
        }