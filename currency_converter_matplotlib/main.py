##-----------------------------------------------------##
##---------------------- imports ----------------------##
import requests
import json
from re import *
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from datetime import datetime, timedelta

##-----------------------------------------------------##
##-------------------- get api url --------------------##
menu = input(" [h] - HISTORY\n [g] - GRAPH\n :")

if menu == "g":
  try:
    base = input("BASE CURRENCY(USD, EUR, GBP...): ")
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
  plt.axis([0, 10, 0, 1])

  ##------------------------------------------------------##
  ##------------ add information on the plots ------------##
  for x,y in zip(xAxis, yAxis):
    label = "{:.3f}".format(y)
    plt.annotate(
      label, # this is the value which we want to label (text)
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

elif menu == "h":
##------------------------------------------------------##
##--------------------- validation for date ---------------------##
  def validate_date(date):
    error = "Invalid Date. It must be in the format YYYY-MM-DD"
    if match(r'^(1[0-2]|0?[1-9])/(3[01]|[12][0-9]|0?[1-9])/(?:[0-9]{2})?[0-9]{2}$', date):
      return date
    else:
      print(error, "\nPLEASE INSER AGAIN: ",end="")
      check=input()
      return validate_date(check)

  ##------------------------------------------------------##
  ##---------------------  get date ---------------------##
  selectedDay = input("ENTER DATE (YYYY-MM-DD): ")
  today = datetime.utcnow().date()
  yesterday = today - timedelta(days=1)

  ##------------------------------------------------------##
  ##---------------------  get currencies ---------------------##
  fr = input("from (USD, EUR, GBP...): ")
  to = input("from (USD, EUR, GBP...): ")

  ##------------------------------------------------------##
  ##--------------------- get info for selected day ---------------------##
  urlSD = "https://api.fastforex.io/historical?date="+selectedDay+"&from="+fr+"&to="+to+"&api_key=c3462e35b9-06f8cc140b-r45w0n"
  responseSD = requests.request("GET", urlSD)
  json_responseSD = responseSD.json()

  with open("selectedDay.json", 'w') as json_fileSD:
    json.dump(json_responseSD, json_fileSD, indent=2)

  dicSD = json.load(open('selectedDay.json', 'r'))

  ##------------------------------------------------------##
  ##--------------------- get info for yesterday ---------------------##
  urlY = "https://api.fastforex.io/historical?date="+str(yesterday)+"&from="+fr+"&to="+to+"&api_key=c3462e35b9-06f8cc140b-r45w0n"
  responseY = requests.request("GET", urlY)
  json_responseY = responseY.json()

  with open("yesterday.json", 'w') as json_fileY:
    json.dump(json_responseY, json_fileY, indent=2)

  dicY = json.load(open('yesterday.json', 'r'))

  ##------------------------------------------------------##
  ##--------------------- get info currency size ---------------------##
  xSD = [key for key, value in json_responseSD["results"].items()]
  ySD = [value for key, value in json_responseSD["results"].items()]
  xY = [key for key, value in json_responseY["results"].items()]
  yY = [value for key, value in json_responseY["results"].items()]

  ##------------------------------------------------------##
  ##--------------------- create plots ---------------------##
  plt.bar("Selected Day", ySD,0.3, align="center", color='b', label=selectedDay +" - "+str(ySD[0]) + " " + str(xSD[0]))
  plt.bar("Yesterday", yY, 0.3,  align="center",  color='g', label=str(yesterday) +" - "+str(yY[0]) + " " + str(xSD[0]))
  plt.legend()
  plt.show()