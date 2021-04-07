
CoolingTypeLimit = { 'PASSIVE_COOLING': {'lowerLimit': 0,'upperLimit':35},
                     'HI_ACTIVE_COOLING': {'lowerLimit': 0,'upperLimit':45},
                     'MED_ACTIVE_COOLING': {'lowerLimit': 0,'upperLimit':40}
                   }

EMailInfo = { 'TOO_LOW' : {'Recepient':'a.b@c.com','Message':'Hi, the temperature is too low'},
              'TOO_HIGH' : {'Recepient':'a.b@c.com','Message':'Hi, the temperature is too high'}
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
  if alertTarget in Alert_Target.keys():
    Alert_Target[alertTarget](breachType)
    return True
  return False

def send_to_controller(breachType):
  print(f'BreachType: {breachType}')

def send_to_email(breachType):
  print(f'Hi {EMailInfo[breachType]['Recepient']} the temperature is {breachType}')

def send_to_console(breachType):
  print(f'BreachType: {breachType}')
  
Alert_Target = { 'TO_CONTROLLER': send_to_controller,
                'TO_EMAIL': send_to_email,
                'TO_CONSOLE': send_to_console }
    
