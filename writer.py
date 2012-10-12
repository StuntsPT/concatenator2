#!/usr/bin/python3
#  Concatenator is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  Concatenator is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
def FASTAWriter(Dict, outfile_name):
	#Writes down the dict as a fasta file
	outfile = open(outfile_name,'w')
	for name,seq in Dict.items():
		newseq = ""
		count = 0
		for i in seq:
			newseq += i
			count += 1
			if count == 60:
				newseq += "\n"
				count = 0
		newseq = newseq.rstrip()
		outfile.write(">" + name + "\n")
		outfile.write(newseq + "\n")
	outfile.close()

def PhylipWriter(Dict, outfile_name):
	#Writes down the dict as a phylip file
	outfile = open(outfile_name,'w')
	maxlen = max(map(len, Dict.keys()))
	outfile.write(" " + str(len(Dict)) + " " + str(len(Dict[list(Dict.keys())[0]])) + "\n")
	for name,seq in Dict.items():
		outfile.write(name)
		outfile.write(" " * (2 + (maxlen - len(name))))
		outfile.write(seq + "\n")
	outfile.close()

def NexusWriter(Dict, outfile_name, datatype="DNA", missingchar="N", gapchar="-"):
	#Writes down the dict as a nexus file
	#The interleave format is now deprecated, so all nexus files are now "leave"
	outfile = open(outfile_name,'w')
	outfile.write("#Nexus\n")
	outfile.write("[" + outfile_name + "] -- data title\n\n")
	outfile.write("Begin data;\n")
	outfile.write(" dimensions ntax=" + str(len(Dict)) + " nchar=" + str(len(Dict[list(Dict.keys())[0]])) + ";\n")
	outfile.write(" format datatype=" + datatype + " interleave=no missing=" + missingchar + " gap=" + gapchar + ";\n")
	outfile.write("  matrix\n")
	for name,seq in Dict.items():
		outfile.write(" ")
		if len(name) < 8: outfile.write(" " * (8 - len(name)) + name)
		else: outfile.write(name[:8])
		outfile.write("  ")
		outfile.write(seq + "\n")
	outfile.write(";\n  end;")
