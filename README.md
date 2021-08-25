# HamariWeb-Bond-Checker
 Checks bonds from draws published on HamariWeb. Use the following command line syntax
 ```
 getpost.py -l:[link to the hamariweb's index to a draw] -r:[optionally give a range using from..to syntax for bond numbers] -f:[path to a file that contains your bond numbers]
 ```
 Either `-f` or `-r` must be present or it would raise an exception.
