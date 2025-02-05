import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..","..","FDE-Tools"))
from HelperFunctions import *
from FDE import *

lon = (-117.7, -117.149)
lat = (32.7071, 32.7216)
print("Loading Map")
if os.path.isfile("SanDiegoMap.npy"):
    L = np.load("SanDiegoMap.npy",allow_pickle=True,encoding="latin1")
else:
    L = LoadMapXML("SanDiego.xml")
    L = [FilterData(l, lon, lat) for l in L]
    np.save("SanDiegoMap.npy", L)
if os.path.isfile("SanDiegoEateries.npy"):
    P = np.load("SanDiegoEateries.npy",allow_pickle=True,encoding="latin1")
else:
    P = GetEateries("SanDiego.xml")
    P = FilterData(P, lon, lat)
    np.save("SanDiegoEateries.npy", P)
print("Declaring fused density estimator")
fde = FDE(L,P)
print("Generating Problem")
fde.GenerateProblem()
print("Solving Problem")
fde.SolveProblem(.022)

#print("Performing Cross Validation...")
#lam = fde.CrossValidate()
#fde.SolveProblem(lam)
#print("Optimal lambda parameter: " + str(lam))
fde.Plot()
plt.show()
