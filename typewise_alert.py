
CoolingTypeLimit = { 'PASSIVE_COOLING': {'lowerLimit': 0,'upperLimit':35},
                     'HI_ACTIVE_COOLING': {'lowerLimit': 0,'upperLimit':45},
                     'MED_ACTIVE_COOLING': {'lowerLimit': 0,'upperLimit':40}
                   }

EMailInfo = { 'TOO_LOW' : {'Recepient':'a.b@c.com','Message':'Hi, the temperature is too low'},
              'TOO_HIGH' : {'Recepient':'a.b@c.com','Message':'Hi, the temperature is too high'}
            }

ControllerInfo = { 'TOO_LOW': 'Heater On',
                  'TOO_HIGH': 'Cooler On'
        }

def compose_email(breachType):
    return { 'To': EMailInfo[breachType]['Recepient'],
             'Subject': breachType,
             'Message':EMailInfo[breachType]['Message']  
            }
    
def compose_controller(breachType):
    return ControllerInfo[breachType]
                          
def email_handle(emailContent):
   print(emailContent)
   return "EMAIL_SENT"    
    
def send_email(emailContent):
   return email_handle(emailContent)

def send_controller(controllerContent,breachType):
    print(f'BreachType: {breachType} action: {controllerContent}')
    return 'CONTROLLER_CALLED'

def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return 'TOO_LOW'
  if value > upperLimit:
    return 'TOO_HIGH'
  return 'NORMAL'

def classify_temperature_breach(coolingType, temperatureInC):
  if coolingType in CoolingTypeLimit.keys():
     coolingType_range = CoolingTypeLimit[coolingType]
     return infer_breach(temperatureInC, coolingType_range['lowerLimit'], coolingType_range['upperLimit'])
  else:
    return 'INVALID_COOLING_TYPE'


def check_and_alert(alertTarget, batteryChar, temperatureInC):
  breachType = classify_temperature_breach(batteryChar['coolingType'], temperatureInC)
  if alertTarget in Alert_Target.keys():
    return Alert_Target[alertTarget](breachType)
  else:
    return 'INVALID_ALERT_TARGET'

def send_to_controller(breachType):
  return send_controller(compose_controller(breachType),breachType)

def send_to_email(breachType):
  return send_email(compose_email(breachType))

def send_to_console(breachType):
  print(f' Console Called --> BreachType: {breachType}')
  return 'CONSOLE_CALLED'
  
Alert_Target = { 'TO_CONTROLLER': send_to_controller,
                'TO_EMAIL': send_to_email,
                'TO_CONSOLE': send_to_console }
    
