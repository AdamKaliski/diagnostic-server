#author Adam Kaliski adam.kaliski47@gmail.com
from flask import Flask
import psutil

app = Flask(__name__)
@app.route('/')

def sysinf():
	cpuperc = psutil.cpu_percent(interval=1)
	cpuresult = "The CPU percentage usage is " + str(cpuperc) + "%"
	memperc = psutil.virtual_memory()[2]
	memresult = "The memory percentage usage is " + str(memperc) + "%" 
	pslist = []
	for proc in psutil.process_iter():
		cpuproc = proc.cpu_percent(interval=1)
		if(cpuproc == 0):
			continue
		else:
			pslist.append([proc.pid, cpuproc])
	pslist.sort(key=lambda x: x[1])#sort by percentage use
	proc_fin = ""
	for ps in reversed(pslist):#reversed because sort sorts it by descending
		p = psutil.Process(ps[0])
		proc_fin += str(ps[0]) + " : " +p.name()+" : CPU percentage: "+str(ps[1]) + "<br/>"
	finalres = cpuresult + "<br/>" + memresult +"<br/>"+proc_fin
	return finalres
		
if __name__ == '__main__':
	app.run()
