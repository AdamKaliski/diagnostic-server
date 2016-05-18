from flask import Flask
import psutil

app = Flask(__name__)
@app.route('/')

def sysinf():
	cpuperc = psutil.cpu_percent(interval=0)
	cpuperc = psutil.cpu_percent(interval=1)
	result = "The CPU percentage usage is " + str(cpuperc) + "%"
	memperc = psutil.virtual_memory()[2]
	memresult = "The memory percentage usage is " + str(memperc) + "%" 
	finalres = result + "<br/>" + memresult
	return finalres
		
if __name__ == '__main__':
	app.run()
