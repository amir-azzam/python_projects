#I know I could have made a class for each char not this shit that I made but it will be a next step Inshallah
import random

#LowerCase
lowerCaseCharOne = chr(random.randint(97,122))
lowerCaseCharTwo = chr(random.randint(97,122))
lowerCaseCharThree = chr(random.randint(97,122))
lowerCaseCharFour = chr(random.randint(97,122))
lowerCaseCharFive = chr(random.randint(97,122))
#UpperCase
upperCaseCharOne = chr(random.randint(65,90))
upperCaseCharTwo = chr(random.randint(65,90))
upperCaseCharThree = chr(random.randint(65,90))
upperCaseCharFour = chr(random.randint(65,90))
upperCaseCharFive = chr(random.randint(65,90))
#Digits
firstDigit = chr(random.randint(48,57))
secondDigit = chr(random.randint(48,57))
thirdDigit = chr(random.randint(48,57))
fourthDigit = chr(random.randint(48,57))
fifthDigit = chr(random.randint(48,57))
#Symbols
firstSymbol = chr(random.randint(33,47))
secondSymbol = chr(random.randint(33,47))
thirdSymbol = chr(random.randint(33,47))
fourthSymbol = chr(random.randint(33,47))
fifthSymbol = chr(random.randint(33,47))

passwordJoin = [
    lowerCaseCharOne,
    lowerCaseCharTwo,
    lowerCaseCharThree,
    lowerCaseCharFour,
    lowerCaseCharFive,
    upperCaseCharOne,
    upperCaseCharTwo,
    upperCaseCharThree,
    upperCaseCharFour,
    upperCaseCharFive,
    firstDigit,
    secondDigit,
    thirdDigit,
    fourthDigit,
    fifthDigit,
    firstSymbol,
    secondSymbol,
    thirdSymbol,
    fourthSymbol,
    fifthSymbol,
]
random.shuffle(passwordJoin)
password = "".join(passwordJoin)
print(password)
