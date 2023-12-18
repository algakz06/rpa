from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Numeric,
    Date
)
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class Active(Base):
    __tablename__ = "active"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class SensorType(Base):
    __tablename__ = "sensor_type"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Sensor(Base):
    __tablename__ = "sensor"

    id = Column(Integer, primary_key=True)
    active_id = Column(Integer, ForeignKey("active.id"))
    type = Column(Integer, ForeignKey("sensor_type.id"))
    name = Column(String)


class ActiveIndex(Base):
    __tablename__ = "active_index"

    id = Column(Integer, primary_key=True)
    active_id = Column(Integer, ForeignKey("active.id"))
    sensors_id = Column(Integer, ForeignKey("sensor.id"))
    value = Column(Numeric)
    measurement_date = Column(Date)
