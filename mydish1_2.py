from flask import Flask
from flask import render_template
import urllib.request as urllib2
import re

app = Flask(__name__)
###########################################
#Minmat.se
#
#TODO:
# Beutify output (understand templates and how to feed them a list)
# Output links instead of text for url's
# Config file with restaurant url/geo coordinate dict
# Make calls with coordinate and distance - search above rest-list
# Implement pluggable views(?)
# Extend website:
#   Landing page - One button-get computer location, one textbox, enter lat-long
#     on action move to
#   second page, Text box, enter food - generate request and goto ~
#   third page, result of above
#    extra - Share link button

# class

class Restaurants:
    def __init__(self, restname, weburl, serves):
        self.rname = restname
        self.wurl = weburl
        self.serv = serves
        self.fexpr = ""
        print("-:: {} ::- created".format(self.rname))

    def __str__(self):
        return self.rname + ", " + self.wurl + ", serves: " + str(self.serv)

    def check_dish(self, fexpr):
        self.fexpr = fexpr;
        print("Checking {} for {}".format(self.rname, self.fexpr))
        site_content = urllib2.urlopen(self.wurl).read()
        if re.search(fexpr, str(site_content)):
            self.serv = True
        

def findish(urls, fexpr):
    for u in urls:
        site_content = urllib2.urlopen(u[1]).read()
        if re.search(fexpr, str(site_content)):
            u[2] = True
    return urls

def buildexpression (exprlist):
    expstr = "|".join(exprlist)
    #for e in exprlist:
    #    expstr += "[{}]".format(e)
    return expststr
            
@app.route('/')
def coremain():
    outstring = "use ~/custom/<YourFavouriteDish>  , regexp can be used."
    return outstring



@app.route('/custom/<food>')
def custom_main(food):
    mydish = food
    searchexpr = ['[Bb]oeuf', '[Kk]roppkak', '[Ii]sterband']
    restaurant = [['Bellevue', 'http://www.restaurangbellevue.se/',False],
                  ['Hotellet', 'http://www.brasserinorrtull.se/frontpage/meny/',False],
                  ['BishopArms', 'http://www.kvartersmenyn.se/rest/14400', False],
                  ['Café Delta', 'http://cafedelta.kvartersmenyn.se/', False]]
    #boefs = findish(restaurant, mydish) #'[Bb]oeuf'  list of expressions
    #bofgen = (b for b in boefs if b[2])
    #print("Denna vecka serveras ", end="")
    #for bo in bofgen:
    #    print(" boeuf på {}\n{}".format(bo[0], bo[1]))  #dynamic and default for no match
    outstring = ""
    restobj = [Restaurants('Snäckhagens', 'https://helagotland.se/lunchguiden/?ShowInfo=1&RestID=10334521/', False),
               Restaurants('Borgen', 'https://bistroborgen.se/dag/',False),
               Restaurants('Märthas', 'https://helagotland.se/lunchguiden/?ShowInfo=1&RestID=8334997/',False),
               Restaurants('Hotellet', 'http://www.brasserinorrtull.se/frontpage/meny/',False),
               Restaurants('BishopArms', 'http://www.kvartersmenyn.se/rest/14400',False),
               Restaurants('Café Delta', 'http://cafedelta.kvartersmenyn.se/', False)]
    #Restaurants('Morkullan', 'http://morkullan.kvartersmenyn.se/',False)-borttagen fr kvartersmenyn
    for r in restobj:
        r.check_dish(mydish)
        #outstring += "{}\n".format(r)
    return render_template('dishtemplate2.html', out=restobj)

if __name__ == '__main__':
    app.run(debug=True)

coremain()
