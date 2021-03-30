import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')
    
  def test_breach_as_per_cooling_type(self):
    self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING',45) == 'TOO_HIGH')

if __name__ == '__main__':
  unittest.main()
