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

def FASTAtoDict(infile_name):
    #Converts the fasta file into a dict {"name":"seq"} and returns it
    infile = open(infile_name,'r')
    Dict={}
    warning = ""
    length = 0
    for lines in infile:
        if lines.startswith('>'):
            name=lines[1:].strip()
            if name in Dict:
                name = name + "2"
                warning = "You have sequences with the same name in your file.\
\nThey have been changed in order the distinguish them, but this is a VERY BAD \
sign that something is wrong and you REALLY should check your file."
            Dict[name]= ''

        elif lines.startswith("\n") == False:
            Dict[name] += lines.strip().upper()

    if warning != "":
        warning = SeqMeasure(Dict)

    infile.close()
    return Dict, warning

def PHYLIPtoDict(infile_name):
    #Converts the phylip file into a dict {"name":"seq"} and returns it
    infile = open(infile_name,'r')
    Dict={}
    infile.readline()
    interleave = 0
    order = []
    warning = ""
    for lines in infile:
        if lines.startswith("\n"):
            interleave = 1
            count = 0
        elif interleave == 0:
            line = lines.split()
            if line[0] in Dict:
                line[0] = line[0] + "2"
                warning = "You have sequences with the same name in your file.\
\nThey have been changed in order the distinguish them, but this is a very BAD \
sign that something is wrong and you REALLY should check your file."
            Dict[line[0]] = "".join(line[1:]).strip()

            order.append(line[0])
        else:
            Dict[order[count]] += lines.replace(" ","").strip()
            count += 1

    if warning != "":
        warning = SeqMeasure(Dict)

    infile.close()
    return Dict, warning

def NEXUXtoDict(infile_name):
    infile = open(infile_name,'r')
    ignore = 1
    Dict = {}
    interleave = 0
    warning = ""
    order = []

    while ignore == 1:
        a = infile.readline()
        if a.strip().startswith("matrix"): ignore = 0

    for lines in infile:
        if lines.strip().startswith(";"):
            break
        elif lines.startswith("\n"):
            interleave = 1
            counter = 0
            continue
        elif interleave == 0:
            line = lines.strip().split(None,1)
            if line[0] in Dict:
                line[0] = line[0] + "2"
                warning = "You have sequences with the same name in your file.\
\nThey have been changed in order the distinguish them, but this is a very BAD \
sign that something is wrong and you REALLY should check your file."
            Dict[line[0]] = line[1].replace(" ", "")
            order.append(line[0])
        else:
            line = lines.strip().split(None,1)
            Dict[order[counter]] += line[1].replace(" ", "")
            counter += 1

    if warning != "":
        warning = SeqMeasure(Dict)

    infile.close()
    return Dict, warning

def SeqMeasure(Dict):
    warning = ""
    for i in Dict.values():
        if length != 0 and len(i) != length:
            warning = "Not all of your sequences have the same length.\nYou \
really should look into this as it is a VERY BAD sign that something is wrong \
if you are using these sequences for further analyses."
        length = len(i)
    return warning
