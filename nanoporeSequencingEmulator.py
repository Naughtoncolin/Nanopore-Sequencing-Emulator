#!/usr/bin/env python3
# Author: Colin Naughton

'''
PSEUDOCODE:
Import pyplot and numpy.
Initialize lists of quadromers with their corresponding expected current with standard deviation.
Ask for sequence from user. (Command at the bottom.)
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
quadromer_data = { #There is more code below this list!
 'AAAA': ('46.2', '1.4'), 'AAAC': ('42.1', '1.3'), 'AAAG': ('48.5', '1.4'), 'AAAT': ('47.3', '1.7'), 'AACA': ('46.8', '1.1'), 'AACC': ('38.7', '0.8'),
 'AACG': ('41.4', '0.9'), 'AACT': ('39.7', '1.0'), 'AAGA': ('48.0', '1.2'), 'AAGC': ('41.4', '1.2'), 'AAGG': ('45.2', '1.2'), 'AAGT': ('43.0', '1.6'),
 'AATA': ('40.1', '0.9'), 'AATC': ('34.1', '1.5'), 'AATG': ('38.7', '1.4'), 'AATT': ('35.4', '1.8'), 'ACAA': ('46.4', '1.3'), 'ACAC': ('43.1', '0.8'),
 'ACAG': ('44.8', '1.0'), 'ACAT': ('45.9', '1.4'), 'ACCA': ('43.0', '1.0'), 'ACCC': ('41.0', '0.9'), 'ACCG': ('45.4', '0.7'), 'ACCT': ('41.5', '1.0'),
 'ACGA': ('46.5', '0.6'), 'ACGC': ('39.9', '1.3'), 'ACGG': ('44.4', '0.8'), 'ACGT': ('41.6', '1.5'), 'ACTA': ('42.1', '1.3'), 'ACTC': ('37.1', '0.8'),
 'ACTG': ('39.3', '1.4'), 'ACTT': ('35.3', '1.7'), 'AGAA': ('55.1', '1.6'), 'AGAC': ('44.6', '1.2'), 'AGAG': ('53.0', '1.3'), 'AGAT': ('49.3', '2.2'),
 'AGCA': ('48.9', '1.5'), 'AGCC': ('41.0', '1.4'), 'AGCG': ('50.4', '1.4'), 'AGCT': ('43.1', '1.1'), 'AGGA': ('47.7', '1.1'), 'AGGC': ('38.8', '1.4'),
 'AGGG': ('40.6', '2.0'), 'AGGT': ('37.6', '1.3'), 'AGTA': ('31.4', '1.4'), 'AGTC': ('23.3', '1.8'), 'AGTG': ('33.8', '1.9'), 'AGTT': ('25.2', '1.4'),
 'ATAA': ('44.5', '0.9'), 'ATAC': ('41.5', '1.0'), 'ATAG': ('42.8', '0.8'), 'ATAT': ('42.3', '0.9'), 'ATCA': ('37.5', '1.1'), 'ATCC': ('34.4', '1.1'),
 'ATCG': ('39.3', '1.0'), 'ATCT': ('37.3', '0.9'), 'ATGA': ('36.4', '1.1'), 'ATGC': ('31.0', '1.0'), 'ATGG': ('35.6', '0.8'), 'ATGT': ('31.7', '1.4'),
 'ATTA': ('31.1', '0.9'), 'ATTC': ('25.0', '1.0'), 'ATTG': ('30.6', '1.2'), 'ATTT': ('0', '0'), 'CAAA': ('46.1', '1.1'), 'CAAC': ('43.1', '1.4'),
 'CAAG': ('46.7', '1.3'), 'CAAT': ('43.3', '1.2'), 'CACA': ('46.9', '1.3'), 'CACC': ('40.3', '1.1'), 'CACG': ('39.4', '1.0'), 'CACT': ('40.8', '0.8'),
 'CAGA': ('47.8', '1.5'), 'CAGC': ('37.1', '1.2'), 'CAGG': ('43.0', '0.8'), 'CAGT': ('39.1', '1.7'), 'CATA': ('42.6', '1.0'), 'CATC': ('35.1', '1.3'),
 'CATG': ('39.4', '1.0'), 'CATT': ('33.1', '2.0'), 'CCAA': ('45.1', '1.0'), 'CCAC': ('42.3', '0.7'), 'CCAG': ('44.0', '1.1'), 'CCAT': ('44.5', '1.3'),
 'CCCA': ('45.5', '1.1'), 'CCCC': ('42.4', '1.2'), 'CCCG': ('43.3', '1.2'), 'CCCT': ('38.0', '1.4'), 'CCGA': ('46.2', '0.9'), 'CCGC': ('40.7', '1.1'),
 'CCGG': ('44.2', '0.8'), 'CCGT': ('37.9', '1.9'), 'CCTA': ('43.8', '0.9'), 'CCTC': ('37.4', '0.9'), 'CCTG': ('35.2', '1.7'), 'CCTT': ('33.6', '1.7'),
 'CGAA': ('50.6', '0.9'), 'CGAC': ('41.8', '1.2'), 'CGAG': ('46.1', '0.7'), 'CGAT': ('44.1', '1.1'), 'CGCA': ('46.4', '1.4'), 'CGCC': ('39.9', '1.0'),
 'CGCG': ('43.5', '0.9'), 'CGCT': ('40.9', '0.8'), 'CGGA': ('39.6', '1.3'), 'CGGC': ('33.8', '1.0'), 'CGGG': ('36.7', '1.8'), 'CGGT': ('31.8', '2.0'),
 'CGTA': ('26.2', '1.5'), 'CGTC': ('16.6', '1.6'), 'CGTG': ('21.4', '1.4'), 'CGTT': ('17.9', '1.3'), 'CTAA': ('46.5', '1.3'), 'CTAC': ('40.1', '0.9'),
 'CTAG': ('44.4', '1.8'), 'CTAT': ('37.5', '1.1'), 'CTCA': ('43.6', '0.9'), 'CTCC': ('37.2', '1.0'), 'CTCG': ('35.7', '2.3'), 'CTCT': ('38.2', '0.9'),
 'CTGA': ('34.5', '1.1'), 'CTGC': ('27.9', '1.0'), 'CTGG': ('33.8', '1.0'), 'CTGT': ('26.1', '2.1'), 'CTTA': ('30.3', '1.0'), 'CTTC': ('22.3', '0.9'),
 'CTTG': ('27.3', '0.8'), 'CTTT': ('23.6', '1.1'), 'GAAA': ('54.3', '1.3'), 'GAAC': ('44.1', '1.1'), 'GAAG': ('49.3', '1.9'), 'GAAT': ('50.0', '1.6'),
 'GACA': ('45.1', '1.2'), 'GACC': ('38.6', '0.9'), 'GACG': ('42.4', '0.9'), 'GACT': ('40.4', '1.5'), 'GAGA': ('49.1', '1.2'), 'GAGC': ('43.4', '1.2'),
 'GAGG': ('43.8', '1.3'), 'GAGT': ('45.2', '1.8'), 'GATA': ('40.5', '0.9'), 'GATC': ('33.9', '2.3'), 'GATG': ('39.2', '1.3'), 'GATT': ('35.1', '1.9'),
 'GCAA': ('48.8', '0.8'), 'GCAC': ('39.1', '1.5'), 'GCAG': ('47.8', '1.4'), 'GCAT': ('38.8', '1.3'), 'GCCA': ('44.7', '0.7'), 'GCCC': ('41.2', '1.4'),
 'GCCG': ('43.9', '1.0'), 'GCCT': ('41.5', '0.8'), 'GCGA': ('47.3', '0.6'), 'GCGC': ('38.8', '1.2'), 'GCGG': ('45.5', '1.0'), 'GCGT': ('38.1', '1.9'),
 'GCTA': ('37.1', '1.3'), 'GCTC': ('34.2', '1.4'), 'GCTG': ('36.6', '1.3'), 'GCTT': ('32.9', '1.6'), 'GGAA': ('52.2', '1.6'), 'GGAC': ('41.5', '1.6'),
 'GGAG': ('47.4', '1.2'), 'GGAT': ('44.3', '1.5'), 'GGCA': ('43.6', '1.7'), 'GGCC': ('39.3', '1.6'), 'GGCG': ('42.2', '1.5'), 'GGCT': ('38.3', '1.8'),
 'GGGA': ('41.3', '1.8'), 'GGGC': ('31.7', '1.5'), 'GGGG': ('31.1', '4.6'), 'GGGT': ('30.9', '2.4'), 'GGTA': ('27.8', '1.8'), 'GGTC': ('17.1', '1.8'),
 'GGTG': ('24.7', '1.3'), 'GGTT': ('19.9', '1.6'), 'GTAA': ('39.3', '1.7'), 'GTAC': ('37.5', '1.9'), 'GTAG': ('38.3', '1.4'), 'GTAT': ('37.2', '1.7'),
 'GTCA': ('35.9', '2.4'), 'GTCC': ('26.3', '2.1'), 'GTCG': ('29.2', '2.0'), 'GTCT': ('27.1', '1.7'), 'GTGA': ('31.7', '2.0'), 'GTGC': ('24.9', '1.8'),
 'GTGG': ('24.0', '1.9'), 'GTGT': ('26.9', '1.4'), 'GTTA': ('27.8', '1.9'), 'GTTC': ('20.1', '1.8'), 'GTTG': ('25.9', '1.6'), 'GTTT': ('21.4', '1.2'),
 'TAAA': ('44.7', '1.2'), 'TAAC': ('42.4', '0.9'), 'TAAG': ('47.5', '1.0'), 'TAAT': ('48.7', '1.2'), 'TACA': ('44.3', '1.4'), 'TACC': ('42.0', '1.2'),
 'TACG': ('42.5', '1.0'), 'TACT': ('43.2', '0.8'), 'TAGA': ('45.3', '1.1'), 'TAGC': ('41.4', '1.0'), 'TAGG': ('44.8', '0.7'), 'TAGT': ('42.9', '1.3'),
 'TATA': ('40.9', '0.9'), 'TATC': ('35.5', '1.0'), 'TATG': ('38.3', '1.2'), 'TATT': ('36.0', '1.1'), 'TCAA': ('43.0', '1.1'), 'TCAC': ('39.0', '1.1'),
 'TCAG': ('44.8', '1.3'), 'TCAT': ('46.5', '1.4'), 'TCCA': ('42.6', '1.3'), 'TCCC': ('39.5', '1.1'), 'TCCG': ('40.8', '1.6'), 'TCCT': ('40.7', '1.0'),
 'TCGA': ('45.2', '2.0'), 'TCGC': ('40.0', '1.2'), 'TCGG': ('41.0', '1.5'), 'TCGT': ('38.9', '1.4'), 'TCTA': ('41.3', '1.2'), 'TCTC': ('34.8', '0.9'),
 'TCTG': ('33.1', '1.3'), 'TCTT': ('33.1', '1.4'), 'TGAA': ('46.0', '2.1'), 'TGAC': ('38.6', '1.1'), 'TGAG': ('43.1', '1.2'), 'TGAT': ('43.3', '1.3'),
 'TGCA': ('42.4', '1.7'), 'TGCC': ('35.9', '1.6'), 'TGCG': ('40.4', '1.7'), 'TGCT': ('37.9', '1.3'), 'TGGA': ('38.6', '1.3'), 'TGGC': ('32.5', '1.1'),
 'TGGG': ('33.8', '1.0'), 'TGGT': ('28.0', '1.7'), 'TGTA': ('27.0', '1.6'), 'TGTC': ('17.1', '1.4'), 'TGTG': ('21.7', '1.1'), 'TGTT': ('18.6', '1.0'),
 'TTAA': ('40.4', '1.6'), 'TTAC': ('35.6', '1.2'), 'TTAG': ('41.2', '1.3'), 'TTAT': ('39.8', '1.1'), 'TTCA': ('34.8', '1.6'), 'TTCC': ('28.6', '1.3'),
 'TTCG': ('32.5', '1.6'), 'TTCT': ('31.6', '1.6'), 'TTGA': ('32.8', '1.2'), 'TTGC': ('27.6', '1.0'), 'TTGG': ('32.0', '1.0'), 'TTGT': ('28.8', '0.8'),
 'TTTA': ('28.3', '1.3'), 'TTTC': ('21.8', '1.1'), 'TTTG': ('26.2', '0.9'), 'TTTT': ('22.8', '0.9')}

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
		plt.title('Expected Current For Sequence Passing Through The Pore') #Labels title.
		plt.subplots_adjust(bottom=0.15) # Adjusts for x-axis label and ticks.
		plt.show() #Shows graph.

sequence = input('Please enter the sequence with you would like to simulate going through the nanopore. Enter the sequence with quotation marks: ')
#sequence = 'TTTTCCTCAGGAATGATTGTGTTTT' #Test sequence.

'''Initialize sequencing emulator object, and plotexpected current trace.'''
referenceSequence = sequencingEmulator(sequence)
referenceSequence.findCurrent()
referenceSequence.plotTrace()
