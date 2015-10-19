__author__ = 'braysher02'

Distance = 100
NameOfRunner = 0
SpeedOfRunner = 0
MStoMPH = 2.24
SpeedInMPH = 0
SpeedLimit = 20

NameOfRunner = input("Name of Runner")
TimeTaken = float(input("Time Taken: "))
SpeedOfRunner = Distance / TimeTaken

SpeedInMPH = SpeedOfRunner * MStoMPH

print (NameOfRunner + " ran the 100m race in: ") + str(round(SpeedInMPH))