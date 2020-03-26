import requests

# Sample 1
#
# import CoronaKit
# print(CoronaKit.Recovered)

# Sample 2
#
# from CoronaKit import *
# print(Cases)

# Sample 3
#
# import CoronaKit
# print("COVID-19 deaths: " + str(CoronaKit.Deaths))

# The CoronaKit.py file needs to be in the same directory as your project.
# REMEMBER: STAY INSIDE AND STAY SAFE

try:
    Covid_Data = requests.get("http://corona.lmao.ninja/all")
    Cases = int(Covid_Data.json()["cases"])
    Deaths = int(Covid_Data.json()["deaths"])
    Recovered = int(Covid_Data.json()["recovered"])
except:
    Cases, Deaths, Recovered = -1

if __name__ == "__main__":
    print("COVID-19 cases: " + str(Cases))
    print("COVID-19 deaths: " + str(Deaths))
    print("COVID-19 recoveries: " + str(Recovered))
    
