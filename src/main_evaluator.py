import json
    
class Evaluator():
    def __init__(self, userID, income):
        self._user = userID
        self._householdIncome = int(income)
        self._incomeCap = 0
        self._maxPercentageToPay = 0.0

        # Requirements
        self._incomeCap = 534000
        self._maxPercentageToPay = 0.06

    def _getIncomeFromMonthly(self, monthlyPayments):
        sum = 0
        for payment in monthlyPayments:
            sum += int(payment)
        sum /= len(monthlyPayments)
        sum *= 12
        return sum


    def _evaluateFreeHours(self):
        # TODO: gjelder kun året det fyller 2, 3, 4, 5
        if (self._householdIncome < self._incomeCap):
            return True
        return False


    def _evaluateMaxPay(self):
        maxPay = self._maxPercentageToPay * self._householdIncome
        return round(maxPay, 2)
                
        
    # Evaluate and dump result 
    def evaluate(self):
        # TODO: inntekstgrunnlag
        data = {
            "valid": self._user != None,
            "userId": self._user,
            "freeHours":  self._evaluateFreeHours(),
            "maxPay": self._evaluateMaxPay()
        }

        return json.dumps(data)