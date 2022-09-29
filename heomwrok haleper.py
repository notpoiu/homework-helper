import random
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

awnsers= ["mer du labrador","mer du beaufort","baie d'hudson","golfe du saint-laurent","golfe du mexique","mer des antilles","mer des sargasses","mer méditéranée","mer nord","mer baltique","mer noire","mer caspénne","mer du japon"," mer du chine","mer de corail","mer d'oman","golfe persique","mer rouge"]

print("Revision Helper - Geographie")
print("made by nathan :o")
print("if you want to quit press CTRL + C")
print(" ")


def MainLoop():
    number = random.choice(numbers)
    print(" ")
    print(f'what is this mer: {number}?')
    awnser = input("Type your awnser: ")
    
    CorrectedAwsner = awnsers[number - 1]
    if(awnser == CorrectedAwsner or awnser in CorrectedAwsner):
        print(" ")
        print("you got it right!")
    else:
        print(" ")
        print("wrong its: " + CorrectedAwsner)
        print("you put: " + awnser)
        

    


while True:

    MainLoop()
