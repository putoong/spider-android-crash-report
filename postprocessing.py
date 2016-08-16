import json

def Log(logMe):
	print "id" + logMe['id'][0] + " found, need further inspection"

def parseText(parseMe):
	strPool = ["system_server", "System_server", "system service", "SYSTEM PROCESS"]
	if any(checkMe in parseMe for checkMe in strPool):
		return 1
	else:
		return 0

def main():
	with open('items.jl') as f:
		for line in f:
			record = json.loads(line)
			if(parseText(record['text'][0]) == 1):
				Log(record)

if __name__ == '__main__':
	main()