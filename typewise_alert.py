
CoolingTypeLimit = { 'PASSIVE_COOLING': {'lowerLimit': 0,'upperLimit':35},
                     'HI_ACTIVE_COOLING': {'lowerLimit': 0,'upperLimit':45},
                     'MED_ACTIVE_COOLING': {'lowerLimit': 0,'upperLimit':40}
                   }

def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return 'TOO_LOW'
  if value > upperLimit:
    return 'TOO_HIGH'
  return 'NORMAL'

def classify_temperature_breach(coolingType, temperatureInC):
  coolingType_range = CoolingTypeLimit[coolingType]
  return infer_breach(temperatureInC, coolingType_range['lowerLimit'], coolingType_range['upperLimit'])


def check_and_alert(alertTarget, batteryChar, temperatureInC):
  breachType = classify_temperature_breach(batteryChar['coolingType'], temperatureInC)
  alert = ('TO_CONTROLLER','TO_EMAIL','TO_CONSOLE')
  for i in alert:
    Alert_Target[alertTarget](breachType)
    return True

def send_to_controller(breachType):
  print(f'BreachType: {breachType}')

def send_to_email(breachType):
  recepient = "a.b@c.com"
  if breachType == 'TOO_LOW':
    print(f'To: {recepient}')
    print('Hi, the temperature is too low')
  elif breachType == 'TOO_HIGH':
    print(f'To: {recepient}')
    print('Hi, the temperature is too high')

def send_to_console(breachType):
  print(f'BreachType: {breachType}')
  
Alert_Target = { 'TO_CONTROLLER': send_to_controller,
                'TO_EMAIL': send_to_email,
                'TO_CONSOLE': send_to_console }
    
