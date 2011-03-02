#!/usr/bin/python

from matplotlib import rc, use
use('Agg')
import math
import sys
import matplotlib.pylab as plt

rc('font',**{'family':'serif','sans-serif':['Helvetica'],'serif':['Times'], 'size':8})
rc('text', usetex=True)
rc('figure', figsize=(2,2))
rc('figure.subplot', left=0.25, top=0.95, bottom=0.2, right=0.9)
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
        
        start = float(fields[4])
        end = float(fields[5])
        worker = fields[11]

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

    duration2 = max_end - min_start

#fig = plt.figure()

#plt.subplots_adjust(wspace=0.2)

ax = plt.subplot(211, frame_on=False, axisbelow=True)
plt.plot(xseries1, yseries1, color='0.6')
plt.xlim(0, math.ceil(max(duration1, duration2)))
plt.ylim(0, 20.5)
#ax.tick_params(top='off', right='off')
plt.xticks([math.ceil(max(duration1, duration2))])
plt.yticks([0, 20], [r'0\%', r'100\%'])
#ax.spines['top'].set_color('none')
#ax.spines['right'].set_color('none')

for tick in ax.yaxis.get_major_ticks():
    tick.tick1On = False
    tick.tick2On = False
    
for tick in ax.xaxis.get_major_ticks():
    tick.tick1On = False
    tick.tick2On = False

ax.axhline(0, linewidth=1, color='0.0')

plt.text(-0.2, 0.5, r'Hadoop', rotation='horizontal', horizontalalignment='center', transform=ax.transAxes)

ax = plt.subplot(212, frame_on=False)
plt.plot(xseries2, yseries2, color='0.0')
plt.xlim(0, math.ceil(max(duration1, duration2)))
plt.ylim(0, 20.5)
#ax.tick_params(top='off', right='off')
plt.xticks([0, math.ceil(duration1), math.ceil(duration2)])
plt.yticks([0, 20], [r'0\%', r'100\%'])
#ax.spines['top'].set_color('none')
#ax.spines['right'].set_color('none')

ax.axhline(0, linewidth=1, color='0.0')


for tick in ax.yaxis.get_major_ticks():
    tick.tick1On = False
    tick.tick2On = False
    
for tick in ax.xaxis.get_major_ticks():
    tick.tick1On = False
    tick.tick2On = False

plt.text(-0.2, 0.5, r'\textsc{Ciel}', rotation='horizontal', horizontalalignment='center', transform=ax.transAxes)
plt.xlabel('Time since start (s)')
plt.xticks((0, math.ceil(min(duration1, duration2))))




plt.savefig('kmeans-cluster-util-100.pdf', format='pdf')
plt.show()
