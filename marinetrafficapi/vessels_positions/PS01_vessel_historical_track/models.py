from marinetrafficapi.models import Model
from marinetrafficapi.fields import NumberField, RealNumberField, DatetimeField, TextField

class VesselHistoricalPosition(Model):
    """Get all vessel historical positions for a specific period of time."""

    mmsi = NumberField(index='MMSI',
                       desc="Maritime Mobile Service Identity - \n"
                            "a nine-digit number sent in digital \n"
                            "form over a radio frequency that \n"
                            "identifies the vessel's transmitter station")

    status = NumberField(index='STATUS',
                         desc="The AIS Navigational Status of the subject \n"
                              "vessel as input by the vessel's crew - more. \n"
                              "There might be discrepancies with the \n"
                              "vessel's detail page when vessel speed is \n"
                              "near zero (0) knots.")

    speed = NumberField(index='SPEED',
                        desc="The speed (in knots x10) that the subject \n"
                             "vessel is reporting according to \n"
                             "AIS transmissions")

    longitude = RealNumberField(index='LON',
                                desc="A geographic coordinate that specifies \n"
                                     "the east-west position of the vessel on \n"
                                     "the Earth's surface")

    latitude = RealNumberField(index='LAT',
                               desc="a geographic coordinate that specifies \n"
                                    "the north-south position of the vessel \n"
                                    "on the Earth's surface")

    course = NumberField(index='COURSE',
                         desc="The course (in degrees) that the subject \n"
                              "vessel is reporting according to \n"
                              "AIS transmissions")

    heading = NumberField(index='HEADING',
                          desc="The heading (in degrees) that the \n"
                               "subject vessel is reporting according \n"
                               "to AIS transmissions")

    timestamp = DatetimeField(index='TIMESTAMP',
                              desc="The date and time (in UTC) that the \n"
                                   "subject vessel's position was recorded \n"
                                   "by MarineTraffic",
                              format='%Y-%m-%dT%H:%M:%S')

    ship_id = NumberField(index='SHIP_ID',
                          desc="A uniquely assigned ID by MarineTraffic \n"
                               "for the subject vessel")
    
    imo = TextField(index='IMO',
                          desc="A uniquely assigned ID by the IMO")

    wind_angle = NumberField(index='WIND_ANGLE',
                             desc="The current angle of the wind in the \n"
                                  "subject area (in degrees, compared \n"
                                  "to True North)")

    wind_speed = NumberField(index='WIND_SPEED',
                             desc="The current wind speed in \n"
                                  "the subject area (in knots)")

    wind_temp = NumberField(index='WIND_TEMP',
                            desc="The current temperature of the wind in \n"
                                 "the subject area (in Celsius degrees)")
    
    sig_wave = NumberField(index='SIGNIFICANT_WAVE_HEIGHT',
                            desc="Significant wave height in the subject area (in meters)")
    
    swell_height = NumberField(index='SWELL_HEIGHT',
                            desc="Swell height in the subject area (in meters)")
    
    swell_period = NumberField(index='SWELL_PERIOD',
                            desc="Swell period in the subject area (in seconds)")
    
    swell_direction = NumberField(index='SWELL_DIRECTION',
                            desc="Swell direction in the subject area (in degrees)")
    
    currents_angle = NumberField(index='CURRENTS_ANGLE',
                            desc="Currents angle in the subject area (in degrees)")
    
    currents_speed = NumberField(index='CURRENTS_SPEED',
                            desc="Currents speed in the subject area (in knots)")
    
    
