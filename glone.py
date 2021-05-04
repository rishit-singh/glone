import numpy
import os
import sys
import json

null = None	#	For convinience

class Tools:
	def CreateCloneAlterArray(value, array: list):
		cloneArray = list()

		for element in array:
			if (element == value):
				continue
			cloneArray.append(element)

		return cloneArray

	def CreateCloneAlterArray(index: int, array: list):
		cloneArray = list()
		arrayLenRange = range(len(array))

		for x in arrayLenRange:
			if (x == index):
				continue

			cloneArray.append(array[x])

		return cloneArray

	def CreateCloneAlterArray(indices: list, array: list):
		cloneArray = list()
		arrayLenRange = range(len(array))

		for x in arrayLenRange:
			if (x in indices):
				continue

			cloneArray.append(array[x])

		return cloneArray

	def ArrayCmp(array : list, array1 : list):
		arraySize = len(array)
		arraySize1 = len(array1)
	
		if (arraySize < arraySize1):
			return bool(0)

		if (arraySize > arraySize1):
			return -1

		if (arraySize == arraySize1):
			for x in range(arraySize):
				if (array[x] != array1[x]):
					return bool(0)

		return bool(1)


class Data:
	DefaultConfigFile = str("~/.glone/config.json")

	GitConfiguration = dict(
		{
			"account" : str(),
			"scm_url" : str()
		}
	)	#	Hash containing the git configuration 

	CommandConfiguration = dict({	#	Stores git commands hashed to glone commands
		"" : "clone",
		"add" : "add -A",  
		"commit" : "commit", 
		"push" : "push",
		"configure" : ""
	})
	
	Commands = numpy.ndarray

	def IsConfigured():	
		return (list(Data.GitConfiguration.values()) != list([str(), str()]))

	def ValidateConfiguration(config: dict, keys: numpy.ndarray):
		Keys = numpy.array(list(config.keys()))

		if (not(Tools.ArrayCmp(keys, Keys))):
			return bool(0)

		for key in Keys:	#	Null check
			if (str(config[key]) == str()):
				return bool(0)
				
		return bool(1)

	def LoadConfiguation():
		FilePointer = null
		ConfigTemp = null

		Data.Commands = numpy.array(list(Data.CommandConfiguration.keys()))		

		try:
			FilePointer = open(os.path.expanduser(Data.DefaultConfigFile), 'r')	
		
			ConfigTemp = json.loads(str(FilePointer.read()))

			if (Data.ValidateConfiguration(ConfigTemp, numpy.array(list(Data.GitConfiguration.keys())))):
				Data.GitConfiguration = ConfigTemp
			else:
				print("Error: Invalid configuration.")
				return bool(0)

			return bool(1)
 
		except FileNotFoundError:
			print(f"Error: glone is not configured, please add the configuration in {Data.DefaultConfigFile}")
			open(os.path.expanduser(Data.DefaultConfigFile), 'w').write(str())	#	Writes an empty string to the newly generated config file


		return bool(0)	


class Program:
	def Clone(repoName: str):
		os.system("git {} {}/{}/{}".format(Data.CommandConfiguration[str()], Data.GitConfiguration[str("scm_url")], Data.GitConfiguration[str("account")], repoName))
	
	FunctionHash = dict({
		"" : Clone
	})

	def ExecuteCommand(command: list):
		if (len(command) > 2):
			try:
				Program.FunctionHash[command[1]](Tools.CreateCloneAlterArray(list([0, 1]), command))

			except KeyError:
				print(f"Error: Invalid commmand \"{command[1]}\"")
				
				return bool(0)
		
		else:
			if (Data.IsConfigured()):
				# print(f"Command array: {Data.Commands}, \nCommand: {command[1]}\n bool: {command[1] in Data.Commands}")
				#if (command[1] in Data.Commands):
				Program.FunctionHash[str()](command[1])
				
				# else:
					# print(f"Error: Invalid command \"{command[1]}\"")
					# 
					# return bool(0)

				return bool(1)
			
			else: 
				print(f"Error: glone is not configured, please add the configuratin in {Data.DefaultConfigFile}.")

			return bool(0)
	
	def Main():
		Data.LoadConfiguation()

		Program.ExecuteCommand(sys.argv)

Program.Main()
