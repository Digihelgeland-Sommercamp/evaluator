import json
    
class Evaluator():
    def __init__(self, rawUserData):
        self._user = None
        self._householdIncome = 0
        self._incomeCap = 0
        self._maxPercentageToPay = 0.0
        self._consumeData(rawUserData)


    def _consumeData(self, rawUserData):
        if rawUserData != None:
            userData = rawUserData

            # with open(rawRequirement) as requriementFile:
            #     requirement = json.load(requriementFile)

            self._user = userData['userId']
            self._householdIncome = userData['income'] if userData['incomeType'] == "Skatt" else self._getIncomeFromMonthly(userData['monthlyIncome'])
            for person in userData['household']:
                personMonthlyIncome = person['monthlyIncome']
                personIncome = person['income'] if person['incomeType'] == "Skatt" else self._getIncomeFromMonthly(personMonthlyIncome)
                self._householdIncome += personIncome
            
            # Requirements
            self._incomeCap = 534000
            self._maxPercentageToPay = 0.06

    def _getIncomeFromMonthly(self, monthlyPayments):
        sum = 0
        for payment in monthlyPayments:
            sum += payment
        sum /= len(monthlyPayments)
        sum *= 12
        return sum


    def _evaluateFreeHours(self):
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

   
