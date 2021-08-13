# Main Evaluator

Main Evaluator is one of multiple micro services for redusert foreldrebetaling. Visit the [main repo](https://github.com/Altinn/summer-camp-2021) to get an overview and read more documentation.

The evaluator has no couplings, but is designed with the needs of "Redusert foreldrebetaling" in mind. 

## API
Every route can be found in [app.py](https://github.com/Digihelgeland-Sommercamp/evaluator/blob/main/app.py) 

* [GET] [/evaluate/\<userID>/\<income>/\<childBirthYear>](https://app.swaggerhub.com/apis/Johannes-s-b/Evaluator/0.1)
   * userID is should be a unique token

## UML
Class diagram of the service
![Class diagram of the service](https://github.com/Altinn/summer-camp-2021/blob/main/Documentation/UML/Evaluator/Evaluator_klassediagram.png "Class diagram of the service")
