#Assignment based on http://www.nasdaq.com/quotes/
#Feel free to use any libraries. 
#Make sure that the output format is perfect as mentioned in the problem.
#Also check the second row of the download dataset.
#If it follows a different format, avoid it or remove it.
import argparse, csv
import numpy as np

def getAttrValues(fileName, attribute):
    attrVals = []
 #Collect proper data
    with open(fileName, 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
	    if attribute == 'close':
		attrVals.append(row[1])
	    elif attribute == 'volume':
		attrVals.append(row[2])
	    elif attribute == 'open':
		attrVals.append(row[3])
	    elif attribute == 'high':
		attrVals.append(row[4])
	    elif attribute == 'low':
		attrVals.append(row[5])
    attrVals = attrVals[1:]
    fvals = [float(i) for i in attrVals]
    return fvals

def normalization ( fileName , normalizationType , attribute):
    '''
    Input Parameters:
        fileName: The comma seperated file that must be considered for the normalization
        attribute: The attribute for which you are performing the normalization
        normalizationType: The type of normalization you are performing
    Output:
        For each line in the input file, print the original "attribute" value and "normalized" value seperated by <TAB> 
    '''
    #TODO: Write code given the Input / Output Paramters.
    values = getAttrValues(fileName, attribute)

    if normalizationType == 'min_max':
        base = min(values)
        rnge = max(values) - base
        normalized = [(x-base)/rnge for x in values]
        for val, normVal in zip(values, normalized):
            print val, "    ", normVal
    elif normalizationType == 'z_score':
        mean = np.mean(values)
        std = np.std(values)
        z_scores = [(x-mean)/std for x in values]
        for val, zVal in zip(values, z_scores):
            print val, "    ", zVal
    else:
	    print 'Please pick a valid normalization type'

def correlation ( attribute1 , fileName1 , attribute2, fileName2 ):
    '''
    Input Parameters:
        attribute1: The attribute you want to consider from file1
        attribute2: The attribute you want to consider from file2
        fileName1: The comma seperated file1
        fileName2: The comma seperated file2
        
    Output:
        Print the correlation coefficient 
    '''
    #TODO: Write code given the Input / Output Paramters.

    vals1 = getAttrValues(fileName1, attribute1)
    vals2 = getAttrValues(fileName2, attribute2)
    corr = np.corrcoef(vals1, vals2)
    print corr[0][1]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Data Mining HW2')
    parser.add_argument('-f1', type=str,
                            help="Location of filename1. Use only f1 when working with only one file.",
                            required=True)
    parser.add_argument("-f2", type=str, 
                            help="Location of filename2. To be used only when there are two files to be compared.",
                            required=False)
    parser.add_argument("-n", type=str, 
                            help="Type of Normalization. Select either min_max or z_score",
                            choices=['min_max','z_score'],
                            required=False)
    parser.add_argument("-a1", type=str, 
                            help="Type of Attribute for filename1. Select either open or high or low or close or volume",
                            choices=['open','high','low','close','volume'],
                            required=False)
    parser.add_argument("-a2", type=str, 
                            help="Type of Attribute for filename2. Select either open or high or low or close or volume",
                            choices=['open','high','low','close','volume'],
                            required=False)



    args = parser.parse_args()

    if ( args.n and args.a1 ):
        normalization( args.f1 , args.n , args.a1 )
    elif ( args.f2 and args.a1 and args.a2):
        correlation ( args.a1 , args.f1 , args.a2 , args.f2 )
    else:
        print "Kindly provide input of the following form:\nKnott_Stefan_HW2.py -f1 <filename1> -a1 <attribute> -n <normalizationType> \nDMPythonHW2.py -f1 <filename1> -a1 <attribute> -f2 <filename2> -a2 <attribute>"
