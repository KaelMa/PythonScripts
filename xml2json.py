import sys
import os
import xmltodict
import json

def convert(xml_file, xml_attribs=True):
    with open(xml_file, "rb") as f:    # notice the "rb" mode
        d = xmltodict.parse(f, xml_attribs=xml_attribs)
        return json.dumps(d, indent=4)

def xmlToJson(path):
    for file in os.listdir(path):
        absFile = os.path.join(path,file)
        if(os.path.isfile(absFile)):
            name,subfix = os.path.splitext(file)
            if (subfix == '.xml'):
                jsonStr = convert(absFile)
                jsonFile = os.path.join(path,name+'.json')
                with open(jsonFile,'w') as dest:
                    dest.write(jsonStr)
        else:
            xmlToJson(absFile)

# main
if __name__ == '__main__':
    if len(sys.argv) <= 1:
        sys.exit()
    file = sys.argv[1]
    xmlToJson(file)
    