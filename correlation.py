import json
import sys
from sys import argv
import math
filename=sys.argv[1]
 
def load_journal(filename): 
 f = open(filename,)
 data = json.load(f)
 return data
 


def compute_phi(data,event):
 TT=0
 for dict in data:
  if event in dict["events"] and dict["squirrel"]==True:
    TT=TT+1

 FF=0
 for dict in data:
   if event not in dict["events"] and dict["squirrel"]==False :
    FF=FF+1
 

 TF=0
 for dict in data:
  if event in dict["events"] and dict["squirrel"]==False: 
   TF=TF+1
 

 FT=0
 for dict in data:
   if event not in dict["events"] and dict["squirrel"]==True :
    FT=FT+1
 
 TO=0
 for dict in data:
  if event in dict["events"]:
    TO=TO+1
 
 FO=0
 for dict in data:
   if event not in dict["events"] :
    FO=FO+1
 
 OT=0
 for dict in data:
   if dict["squirrel"]==True :
    OT=OT+1
 

 OF=0
 for dict in data:
   if dict["squirrel"]==False :
    OF=OF+1


 phi = (TT * FF -TF * FT) / math.sqrt(TO * FO * OT * OF)
 return phi


 
  
def compute_correlations(filename):
  my_list=[]
  my_dict={}
  data=load_journal(filename)
  for dict in data:
   for event in dict["events"]:
    if event not in my_list:
     my_list.append(event)
     phi=compute_phi(data,event)
     my_dict[event]=phi
  return my_dict 


def diagnose(filename):
 my_dict=compute_correlations(filename)
 max_key = max(my_dict, key=my_dict.get)
 min_key = min(my_dict, key=my_dict.get)
 return max_key,min_key

