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

def filetype(infile_name):
	#Detects the type of file to be parsed
	autofind = "unknown"
	infile = open(infile_name,'r')
	header = infile.readline()
	phy_header = header.strip().split()
	if header.upper().startswith("#NEXUS"):
		autofind = "nexus"
		return autofind
	elif len(phy_header) == 2 and phy_header[0].isdigit():
		autofind = "phylip"
		return autofind
	elif header.startswith(">"):
		autofind = "fasta"
		return autofind
	elif header.startswith("\n"):
		header = infile.readline()
		if header.startswith(">"):
			autofind = "fasta"
			return autofind

	infile.close()
	return autofind

