import requests, urllib, json

x = "http://api.smmry.com/SM_API_KEY=B82922E9B1"

y = raw_input("Enter URL")
z = raw_input("Enter Length of Summary")

final = x + "&SM_LENGTH=" + z + "&SM_URL=" + y 

print (final)

response = requests.get(final)
data = response.text

titlefind = "\"sm_api_title\""
infofind = "\"sm_api_content\""
endofinfo = "\"sm_api_limitation\""
start = data.find(titlefind)
end = data.find(infofind)
enddata = data.find(endofinfo)
title = data[start+16:end-2]
print title

info = data[end+19:enddata-2]
print info

f = open(str(title) + ".txt", "w+")

f.write(info)
f.close()
