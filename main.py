from flask import Flask #Flask permitirá crea la aplicación
#from flask_sqlalchemy import SQLAlchemy #Importar SQLAlchemy para poder crear los modelos
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timezone


#Crear una instancia en la clase Flask
app = Flask(__name__) #Se inicaliza la aplicación

#Decorador route() para asignar la URL a una función que se activará cuando el navegador se encuentr en esa url
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#Crear la conexión a la base de datos
engine = create_engine("postgresql://default:BXqN8wPv6KHW@ep-royal-fire-a485ftso.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require")

#Crear la sesión
Session = sessionmaker(bind = engine)
session = Session()

#Crear la base declarativa
Base = declarative_base()

#Definir el modelo para la tabla taxis
class Taxis(Base):
    __tablename__ = 'taxis' #Nombre de la tabla que ya existe
    id = Column(Integer, primary_key=True)
    plate = Column(String, unique=True, nullable=False)

#Definir el modelo de tabla para las trayectorias
class Trajectories(Base):
    __tablename__ = 'trajectories'
    id = Column(Integer, primary_key=True)
    taxi_id = Column(Integer, ForeignKey('taxis.id'))
    date = Column(DateTime, default=lambda: datetime.now())
    latitude = Column(Float)
    longitude = Column(Float)

#Crear las tablas
Base.metadata.create_all(engine)

if __name__ == "__main__":
    app.run(debug=True)
