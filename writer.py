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
def FASTAwriter(Dict,outfile_name):
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
