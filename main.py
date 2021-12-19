# CURRENCY CONVERTER ALL

##-----------------------------------------------------##
##---------------------- imports ----------------------##
import matplotlib.pyplot as plt
import json
import requests
import json
from matplotlib.widgets import Slider

##-----------------------------------------------------##
##-------------------- get api url --------------------##
try:
  base = input("Base currency: ")
  url = "https://api.fastforex.io/fetch-all?from="+base+"&api_key=c3462e35b9-06f8cc140b-r45w0n"
  response = requests.request("GET", url)
  json_response = response.json()


##-----------------------------------------------------##
##------------------ sort currencies ------------------##
  sorted_all_currencies = {}
  for k in sorted(json_response["results"], key=json_response["results"].get):
      sorted_all_currencies[k] = json_response["results"][k]
      # remove value if greater than 2000
      if sorted_all_currencies[k] > 2000:
          del sorted_all_currencies[k]
except:
  print(base, "CURRENCY NOT FOUND!")
##-----------------------------------------------------##
##------------- add values into json file -------------##
with open("currency.json", 'w') as json_file:
    json.dump(sorted_all_currencies, json_file, indent=2)

##------------- get values from json file -------------##
dic = json.load(open('currency.json', 'r'))

##-----------------------------------------------------##
##---------------- get info for X axis ----------------##
xAxis = [key for key, value in dic.items()]

##-----------------------------------------------------##
##---------------- get info for Y axis ----------------##
yAxis = [value for key, value in dic.items()]
fig, ax = plt.subplots()
##-----------------------------------------------------##
##----------------- create a bar graph ----------------##
plt.bar(xAxis, yAxis, color='maroon')
plt.title(base)
plt.axis([0, 10, -1, 1])

##------------------------------------------------------##
##------------ add information on the plots ------------##
for x,y in zip(xAxis, yAxis):
    label = "{:.3f}".format(y)
    plt.annotate(label, # this is the value which we want to label (text)
                 (x,y), # x and y is the points location where we have to label
                 textcoords="offset points",
                 xytext=(0,10), # this for the distance between the points
                 # and the text label
                 ha='center',
                 arrowprops=dict(arrowstyle="->", color='black'))


##------------------------------------------------------##
##---------------------  scrollbar ---------------------##
axcolor = 'lightgoldenrodyellow'
axpos = plt.axes([0.1, 0.01, 0.65, 0.03], facecolor=axcolor)
spos = Slider(axpos, 'Pos', 0.10, len(xAxis))


##------------------------------------------------------##
##-------------------- adding field --------------------##
def update(val):
    pos = spos.val
    ax.axis([pos,pos+10,-1,2000])
    fig.canvas.draw_idle() 
spos.on_changed(update)

plt.show()

# try it on your local pc, and open comments with *
