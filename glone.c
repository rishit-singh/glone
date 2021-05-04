// Generates a binary.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char** argv)
{
	if (argc < 2)	//	Argument check.
	{
		printf("Insufficient arguments.\n");

		return -1;
	}
	
	char* command = (char*)malloc(sizeof(char) * 100),
		*commandName = "python3 ~/.glone/glone.py";
	
	strcat(command, commandName);
	
	for (int x = 1; x < argc; x++)
		strcat(strcat(command, " "), argv[x]);

	system(command);

	free(command);

	return 0;
}

