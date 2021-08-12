import datetime
import json
from datetime import datetime
from datetime import date

class Evaluator():
    def __init__(self, userID, income, child_birth_year):
        self._user = userID
        self._householdIncome = int(income)
        self._incomeCap = 0
        self._maxPercentageToPay = 0.0
        self.birth_year = datetime.strptime(child_birth_year, '%Y').year

        # Requirements
        self._incomeCap = 583650
        self._maxPercentageToPay = 0.06

    # Evaluates if the household qualifies for "gratis kjernetid"
    def _evaluateFreeHours(self):
        # Returns false if the child does not become 2, 3, 4 or 5 years old this year
        current_year = date.today().year
        age = current_year - self.birth_year
        if age < 2 or age > 5:
            return False

        if (self._householdIncome < self._incomeCap):
            return True

        return False


    def _evaluateMaxPay(self):
        maxPay = self._maxPercentageToPay * self._householdIncome
        return round(maxPay, 2)
                
        
    # Evaluate and dump result 
    def evaluate(self):
        data = {
            "valid": self._user != None,
            "userId": self._user,
            "freeHours":  self._evaluateFreeHours(),
            "maxPay": self._evaluateMaxPay()
        }

        return json.dumps(data)