import random
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

awnsers= ["mer du labrador","mer du beaufort","baie d'hudson","golfe du saint-laurent","golfe du mexique","mer des antilles","mer des sargasses","mer méditéranée","mer nord","mer baltique","mer noire","mer caspénne","mer du japon"," mer du chine","mer de corail","mer d'oman","golfe persique","mer rouge"]

print("Revision Helper - Geographie")
print("made by nathan :o")
print(" ")

afterhowmuch = input(f"how much times do you want to repeat this untill i interup\nyou to ask you to coninue? Type here: ")
afterhowmuchint = int(afterhowmuch)

index = 0

def MainLoop():
    number = random.choice(numbers)
    print(" ")
    print(f'what is this mer: {number}?')
    awnser = input("Type your awnser: ")
    
    CorrectedAwsner = awnsers[number - 1]
    if(String.lower(awnser) == String.lower(CorrectedAwsner) or String.lower(awnser) in String.lower(CorrectedAwsner)):
        print(" ")
        print("you got it right!")
    else:
        print(" ")
        print("wrong its: " + CorrectedAwsner)
        print("you put: " + awnser)
        

    


while True:
    if(index is afterhowmuchint):
        print("interupted!")
        print("if you want to stop the helper then press ctrl + c or else awnser this below:")
        print(" ")
        afterhowmuch = input(f"how much times do you want to repeat this untill i interup\nyou to ask you to coninue? Type here: ")
        afterhowmuchint = int(afterhowmuch)
    else:
        index += 1

    MainLoop()
