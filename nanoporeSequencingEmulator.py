#!/usr/bin/env python3
# Author: Colin Naughton

'''
PSEUDOCODE:
Import pyplot.
Initialize lists of quadromers with their corresponding expected current with standard deviation.
Ask for sequence from user.
Create sequence emulator object from given sequence.
	Cast sequence in upper case.
	Make list of all quadromers in the sequence.
Create list of expected current values with standard deviation for each quadromer.
Plot current trace with graph labels.
	Determine x-axis points.
		Determine y-axis points.
	Set graph labels and ticks.
	Plot
'''

import matplotlib.pyplot as plt
import numpy as np
from quadromers import quadromer_data

class sequencingEmulator:
	'''
	Models a strand of DNA and determine expected current output through nanopore.

	Keyword arguements:
	strand = Sequence of the strand to be emulated.
	'''
	def __init__(self, strand):
		'''Initialize the sequence, its quadromer substrings, and current/trace info.'''
		self.seq = strand.upper()
		self.quadromerList = [self.seq[i:i + 4] for i in range(0, len(self.seq)-3)]
		self.traceCurrentpA = [] #List of expected current values.
		self.standardDeviationpA = [] #List of standard deviation of expected current values.
		self.xAxisPoints = [] 
		self.yAxisPoints = []

	def findCurrent(self):
		'''Finds expected current values with standard deviation for each quadromer in sequence.
		Searches for list containing these values based on the first nucleotide of the quadromer.'''
		for quadromer in self.quadromerList:
			self.traceCurrentpA.append(quadromer_data[quadromer][0])
			self.standardDeviationpA.append(quadromer_data[quadromer][1])

	def plotTrace(self):
		'''Plots expected currents as a trace on a graph using current for the y-axis, and the different quadromers
		in order on the x-axis.'''
		for i in range(len(self.traceCurrentpA)): #Determines x points based on total # of quadromers, with 10 points for each.
			self.xAxisPoints.extend([ i+k*0.01 for k in range(100)])
			self.yAxisPoints.extend(np.random.normal(self.traceCurrentpA[i], self.standardDeviationpA[i], 100))

		ticks= [(i+0.5) for i in range(len(self.traceCurrentpA))] #Determines placement of each quadromer under its expected current trace.
		plt.plot(self.xAxisPoints, self.yAxisPoints) #Plots points in backround.
		plt.xticks(ticks, self.quadromerList, rotation='vertical') #Labels each quadromer position w/ correct quadromer in vertical position.
		plt.xlabel(self.seq) #Places the orginal sequence as the x-axis label.
		plt.ylabel('Current (pA)') #Labels y-axes with current in picoamps.
		plt.title('Quadromer Induced Current Values Through Nanopore') #Labels title.
		plt.subplots_adjust(bottom=0.15) # Adjusts for x-axis label and ticks.
		plt.show() #Shows graph.

#sequence = input('Please enter the sequence you would like to simulate going through the nanopore: ')
sequence = 'TTTTCCTCAGGAATGATTGTGTTTT' #Test sequence.

'''Initialize sequencing emulator object, and plotexpected current trace.'''
referenceSequence = sequencingEmulator(sequence)
referenceSequence.findCurrent()
referenceSequence.plotTrace()
