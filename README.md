# Main Evaluator

Main Evaluator is one of multiple micro services for redusert foreldrebetaling. Visit the [main repo](https://github.com/Altinn/summer-camp-2021) to get an overview and read more documentation.

The evaluator has no couplings, but is designed with the needs of "Redusert foreldrebetaling" in mind. 

## API
Every route can be found in [app.py](https://github.com/Digihelgeland-Sommercamp/evaluator/blob/main/app.py) 

* [GET] [/evaluate/\<userID>/\<income>]()
   * userID is should be a unique token

TODO: LAG SWAGGER OPENAPI DOCS