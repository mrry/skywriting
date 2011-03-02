#!/usr/bin/python

from matplotlib import rc, use
use('Agg')
import math
import sys
import matplotlib.pylab as plt

rc('font',**{'family':'serif','sans-serif':['Helvetica'],'serif':['Times'], 'size':8})
rc('text', usetex=True)
rc('figure', figsize=(3,2))
rc('figure.subplot', left=0.2, right=0.95, top=0.95, bottom=0.2)
rc('axes', linewidth=0.5)
rc('lines', linewidth=0.5)


with open(sys.argv[1]) as first:

    first.readline()
    
    min_start = None
    max_end = None
    
    worker_bars = {}
    
    events = []
    
    for line in first.readlines():
        fields = line.split()
        
        try:
            start = float(fields[4])
            end = float(fields[5])
            worker = fields[11]
        except:
            continue

        events.append((start, 1, worker))
        events.append((end, -1, worker))

        min_start = start if min_start is None else min(min_start, start)
        max_end = end if max_end is None else max(max_end, end)

    events.sort()

    xseries1 = []
    yseries1 = []
    active_workers = {}

    for t, delta, w in events:
        xseries1.append(t - min_start)
        yseries1.append(len(active_workers))
        try:
            active_workers[w] += delta
            if active_workers[w] == 0:
                del active_workers[w]
        except KeyError:
            active_workers[w] = delta
        xseries1.append(t - min_start)
        yseries1.append(len(active_workers))

    duration1 = max_end - min_start

with open(sys.argv[2]) as second:

    second.readline()
    
    min_start = None
    max_end = None
    
    worker_bars = {}
    
    events = []
    
    for line in second.readlines():
        fields = line.split()
        
        try:
            start = float(fields[4])
            end = float(fields[5])
            worker = fields[11]
        except:
            continue

        events.append((start, 1, worker))
        events.append((end, -1, worker))

        min_start = start if min_start is None else min(min_start, start)
        max_end = end if max_end is None else max(max_end, end)

    events.sort()

    xseries2 = []
    yseries2 = []
    active_workers = {}

    for t, delta, w in events:
        xseries2.append(t - min_start)
        yseries2.append(len(active_workers))
        try:
            active_workers[w] += delta
            if active_workers[w] == 0:
                del active_workers[w]
        except KeyError:
            active_workers[w] = delta
        xseries2.append(t - min_start)
        yseries2.append(len(active_workers))

        print t - min_start, len(active_workers)

    

    duration2 = max_end - min_start

#fig = plt.figure()

#plt.subplots_adjust(wspace=0.5)

ax = plt.subplot(211, frame_on=False, axisbelow=True)
plt.plot(xseries1, yseries1, color='0.0')
plt.ylim(0, 21)
#ax.tick_params(top='off', right='off')
plt.xticks([])
plt.xticks([math.ceil(duration1)])
plt.yticks([0, 20], ['0\%', '100\%'])
#ax.spines['top'].set_color('none')
#ax.spines['right'].set_color('none')
#ax.axvline(0,color='black')
ax.axhline(0, color='black', linewidth=1.0)

plt.ylabel(r'\centering No \linebreak \centering failure', rotation='horizontal', ha='center')

for tick in ax.yaxis.get_major_ticks():
    tick.tick1On = False
    tick.tick2On = False
    
for tick in ax.xaxis.get_major_ticks():
    tick.tick1On = False
    tick.tick2On = False

plt.xlim(0, math.ceil(max(duration1, duration2)))


ax = plt.subplot(212, frame_on=False)
plt.plot(xseries2, yseries2, color='0.0')
#ax.tick_params(top='off', right='off')
plt.yticks([0, 20], ['0\%', '100\%'])
#ax.axvline(0, color='black', linewidth=1.0)
ax.axhline(0, color='black', linewidth=1.0)
#ax.spines['top'].set_color('none')
#ax.spines['right'].set_color('none')

for tick in ax.yaxis.get_major_ticks():
    tick.tick1On = False
    tick.tick2On = False
    
for tick in ax.xaxis.get_major_ticks():
    tick.tick1On = False
    tick.tick2On = False

FAIL_START = 63.0199999809
FAIL_END = 70.7000000477

ax.bar(FAIL_START, 20, width=FAIL_END-FAIL_START, color='0.8', linewidth=0)

#ax.text(FAIL_START + (FAIL_END-FAIL_START)/2.0, 0, 'Downtime', ha='center', fontsize=6)

#ax.annotate(r'Downtime', xy=(FAIL_START + (FAIL_END-FAIL_START)/2.0, 5), xytext=((FAIL_START + (FAIL_END-FAIL_START)/2.0,-5)), arrowprops={'arrowstyle':"->", 'linewidth':0.5}, fontsize=6, ha='center')

arr = ax.annotate('', xy=(FAIL_START + (FAIL_END-FAIL_START)/2.0, 5), xytext=(FAIL_START + (FAIL_END-FAIL_START)/2.0, -4), arrowprops={'arrowstyle':"->", 'linewidth':0.5})
ax.text(FAIL_START + (FAIL_END-FAIL_START)/2.0, -4, r'Downtime', fontsize=6, ha='center')

plt.ylabel(r'\centering Master \linebreak failure', rotation='horizontal', ha='center')
plt.xlabel('Time since start (s)')


plt.xlim(0, math.ceil(max(duration1, duration2)))
plt.ylim(0, 21)

plt.xticks([0, math.ceil(duration2)])


#ax.axvline(FAIL_START, 0, 0.5, color='black')
#ax.axvline(FAIL_END, 0, 0.5, color='black')


plt.savefig('bsp-fault-tolerance.pdf', format='pdf')
plt.show()
