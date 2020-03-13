#!/usr/bin/env python
import sys
import argparse

parser = argparse.ArgumentParser(description='''Generate a curl command to retreive data from JGI using the html file for any given project.  You can retrieve anyting from assemblies to the raw reads and taxonomy etc.''')
parser.add_argument('-html', help = 'The html file of a project that contains all of the links to the data for a project contained in the JGI repo')
parser.add_argument('-out', help = 'The name of the outfile to write the curl commands as a bash script. .shx will be appended to the outfile name')
parser.add_argument('-keyword', help = 'The type of data that you are interested in.  For example "assembly.contigs.fasta".  This is an important param and should be tested using grep etc to make sure that you will return the file of interest from the html file')
args = parser.parse_args()

htmlf = open(args.html, 'r')
outfile = open(args.out, 'w')

outfile.write("#!/bin/bash"+'\n')

for line in htmlf:
    x = line.strip('"')
    if args.keyword in x:
        for element in x.split():
            if "url" in element:
                outfile.write("curl 'https://genome.jgi.doe.gov" + element.split('"')[1] + "'" + ' -b cookies > ' + x.split()[0].split('"')[1]+'_'+args.keyword+'\n')





 
