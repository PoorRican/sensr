class Pump(object):
  def __init__(self, pin, timing):
    ''' timing: time required to run pump '''
    self.pin = pin
    self.timing = timing

  def run(self, timing=None):
    if not timing:
      timing = self.timing

    # run for time
    return None


class Valve(object):
  def __init__(self, pin):
    self.pin = pin

  def open(self):
    # send open voltage
    return None

  def close(self):
    # send close voltge
    return None


class PrismController(object):
  def __init__(self, motor_pin, encoder_pin):
    self.motor_pin = motor_pin
    self.encoder_pin

  def calibrate(self, optical_sensor):
    # reset min max
    # verify
    return None

  def transmit(self, wavelen):
    return None


class OpticalSensor(object):
  def __init__(self, pin):
    self.pin

  def read(self):
    # read pin, return value
    return 0.0


class Compound(object):
  def __init__(self, name, wavelen, data=None):
    self.name = name
    self.wavelen = wavelen
    self.data = data
    self.m, self.b = 0,0
    self.regress()

  def regress(self):
    # perform regression
    return None

  def add(self, concentration, opacity):
    data = np.array((concentration, opacity))
    if not self.data:
      self.data = data
    else:
      self.data = np.concatenate(self.data, data)

    self.regress()

  def approximate(self, opacity):
    # TODO: check if opacity is within bounds of data
    return self.m * opacity + self.b


class ReagentTest(object):
  def __init__(self):
    return None

  def add_reagent(self):
    # open reagent valve
    # close fraction valve
    # close purge valve
    # open reaction vessel inlet valve
    # pump reagent
    # close reagent valve
    return None

  def purge(self):
    # close reagent valve
    # open reaction vessel inlet valve
    # open fraction valve
    # pump fraction
    # close fraction valve
    # open reaction vessel outlet valve
    # open argon valve
    # open purge valve
    # close argon valve
    # close purge valve
    return None

  def collect_fraction(self):
    # open reaction vessel inlet valve
    # open fraction valve
    # pump fraction
    # close fraction valve
    return None

  def test(self):
    self.purge()
    self.collect_fraction()
    self.add_reagent()
    opacity = self.sensor.read()
    self.purge()
    return opacity

gggg
