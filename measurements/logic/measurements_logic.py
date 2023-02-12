from datetime import datetime
from ..models import Measurement
from ..models import Variable

def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(measurement_pk):
    measurement = Measurement.objects.get(pk=measurement_pk)
    return measurement

def update_measurement(measurement_pk, new_measurement):
    measurement = get_measurement(measurement_pk)
    measurement.variable = Variable.objects.get(pk=new_measurement["variable"]) 
    measurement.value = new_measurement["value"]
    measurement.unit = new_measurement["unit"]
    measurement.place = new_measurement["place"]
    measurement.save()
    return measurement

def create_measurement(measurement):
    measurement = Measurement(
        variable=Variable.objects.get(pk=measurement["variable"]),
        value=measurement["value"],
        unit=measurement["unit"],
        place=measurement["place"])
    measurement.save()
    return measurement

def delete_measurement(measurement_pk):
    measurement = get_measurement(measurement_pk)
    measurement.delete()
    return measurement