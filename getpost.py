import io
import urllib.request
from sys import argv
import argparse
from bs4 import BeautifulSoup

ap = argparse.ArgumentParser()
ap.add_argument("-l", "--link", required=True, help="Link to a hamariweb draw")
ap.add_argument("-r", "--range", required=False, help="Series of numbers in format from..to")
ap.add_argument("-f", "--file", required=False, help="Path to file")
args = vars(ap.parse_args())

def preprocess_links(dictionary):
    new_dict = {}
    for k, v in dictionary.items():
        if not (v is None):
            new_dict[k] = dictionary[k][1:]
    return new_dict

if not (("range" in args) or ("file" in args)):
    raise Exception("Expected either range or file")

args = preprocess_links(args)

def getList(content, row_name):
    prices = set()

    soup = BeautifulSoup(content, features="html.parser")

    for elem in soup.find_all("td", {'class': row_name}): 
        prices.add(int(elem.renderContents().strip()))

    return prices

def printNPrices(label, ls, bs):
    print(label)
    for b in bs:
        if ls.__contains__(b): print(b)

# hamariweb link
link = args["link"]
print("----")
req = urllib.request.Request(link, headers={'User-Agent': 'Mozilla/5.0'})
data = urllib.request.urlopen(req).read()
print("____")
firsts = getList(data, "first_td")
seconds = getList(data, "second_td")
thirds = getList(data, "third_td")

bonds = []

if "file" in args:
    with open(args["file"]) as b:
        bonds += [int(x.strip()) for x in b.readlines() if x != "\n"]

if "range" in args:
    range_bonds = args["range"].split("..")
    range_bonds_int = list(map(int, range_bonds))
    bonds += list(range(range_bonds_int[0], range_bonds_int[1]))

printNPrices("First", firsts, bonds)
printNPrices("Second", seconds, bonds)
printNPrices("Third", thirds, bonds)