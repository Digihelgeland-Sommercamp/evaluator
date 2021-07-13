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

            self.user = userData['userId']
            self.householdIncome = userData['income'] if userData['incomeType'] == "Skatt" else self._getIncomeFromMonthly(userData['monthlyIncome'])
            for person in userData['household']:
                personMonthlyIncome = person['monthlyIncome']
                personIncome = person['income'] if person['incomeType'] == "Skatt" else self._getIncomeFromMonthly(personMonthlyIncome)
                self.householdIncome += personIncome
            
            # Requirements
            self.incomeCap = 534000
            self.maxPercentageToPay = 0.06

    def _getIncomeFromMonthly(self, monthlyPayments):
        sum = 0
        for payment in monthlyPayments:
            sum += payment
        sum /= len(monthlyPayments)
        sum *= 12
        return sum


    def _evaluateFreeHours(self):
        if (self.householdIncome < self.incomeCap):
            return True
        return False


    def _evaluateMaxPay(self):
        maxPay = self.maxPercentageToPay * self.householdIncome
        return round(maxPay, 2)
                
        
    # Evaluate and dump result 
    def evaluate(self):
        data = {
            "valid": self.user != None,
            "userId": self.user,
            "freeHours":  self._evaluateFreeHours(),
            "maxPay": self._evaluateMaxPay()
        }

        return json.dumps(data)

    # Property user identificator
    @property
    def user(self):
        return self._user

    @user.setter
    def setUser(self, value):
        self._user = value

    # Property householdincome
    @property
    def householdIncome(self):
        return self._householdIncome

    @user.setter
    def setHouseholdIncome(self, value):
        self._householdIncome = value
 

    # Property incomeCap
    @property
    def incomeCap(self):
        return self._incomeCap

    @user.setter
    def setIncomeCap(self, value):
        self._incomeCap = value
    

    # Property maxPercentageToPay
    @property
    def maxPercentageToPay(self):
        return self._maxPercentageToPay

    @user.setter
    def setMaxPercentageToPay(self, value):
        self._maxPercentageToPay = value
