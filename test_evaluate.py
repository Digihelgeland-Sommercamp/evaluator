import unittest
import json

import src.main_evaluator as eval


class TestEvalute(unittest.TestCase):
        

    def test_consumeData(self):
        testDataFile= open('userData.json')
        self.user_data = json.load(testDataFile)
        testDataFile.close()
        self._evaluator = eval.Evaluator(self.user_data)
        
        self.assertEqual(self._evaluator._user, 1, "User Id should be 1")
        self.assertEqual(self._evaluator._householdIncome, 100000, "Household income should be 260k")
        self.assertEqual(self._evaluator._incomeCap, 534000, "Income cap should be 534000")
        self.assertEqual(self._evaluator._maxPercentageToPay, 0.06, "Max percentage should be 0.06")
    
    def test_evaluate(self):
        testDataFile= open('userData.json')
        self.user_data = json.load(testDataFile)
        testDataFile.close()
        self._evaluator = eval.Evaluator(self.user_data)
        
        expectedData = {
            "valid": True,
            "userId": 1,
            "freeHours":  True,
            "maxPay": 6000
        }
        self.assertDictEqual(json.loads(self._evaluator.evaluate()), expectedData, \
            "Data should be 'valid': True,'userId': 1,'freeHours':  True,'maxPay': 6000")
        

if __name__ == '__main__':
    unittest.main()