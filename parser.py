#!/usr/bin/python3
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#

def FASTAtoDict(infile):
    #Converts the fasta file into a dict {"name":"seq"} and returns it
    Dict={}
    for lines in infile:
        if lines.startswith('>'):
            name=lines[1:].strip()
            Dict[name]= ''
        elif lines.startswith("\n") == False:
            Dict[name] += lines.strip().upper()
    infile.close()
    return Dict

def PHYLIPtoDict(infile):
    #Converts the phylip file into a dict {"name":"seq"} and returns it
    Dict={}
    infile.readline()
    interleave = 0
    order = []
    for lines in infile:
        if lines.startswith("\n"):
            interleave = 1
            count = 0
        elif interleave == 0:
            line = lines.split()
            Dict[line[0]] = "".join(line[1:]).strip()
            order.append(line[0])
        else:
            Dict[order[count]] += lines.replace(" ","").strip()
            count += 1
    infile.close()
    return Dict

testfile = "Testfiles/Beta.phy"
testfile = open(testfile,'r')

phylip = PHYLIPtoDict(testfile)
fasta = FASTAtoDict(open("Testfiles/Beta.fas","r"))

if phylip == fasta:
    print("OK!")
