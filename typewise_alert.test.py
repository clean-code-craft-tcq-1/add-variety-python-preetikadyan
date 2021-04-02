import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')
    self.assertTrue(typewise_alert.infer_breach(40, 10, 30) == 'TOO_HIGH')
    self.assertTrue(typewise_alert.infer_breach(40, 20, 60) == 'NORMAL')
    
    
  def test_breach_as_per_cooling_type(self):
    self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING',45) == 'TOO_HIGH')
    self.assertTrue(typewise_alert.classify_temperature_breach('HI_ACTIVE_COOLING',-5) == 'TOO_LOW')
    self.assertTrue(typewise_alert.classify_temperature_breach('MED_ACTIVE_COOLING',20) == 'NORMAL')
    
  def test_check_and_alert(self):
    self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER',{'coolingType':'PASSIVE_COOLING'},70)== True)
    

if __name__ == '__main__':
  unittest.main()
