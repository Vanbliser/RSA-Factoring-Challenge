#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main(int argc, char **argv)
{
	char *lineptr, *endptr, *number;
	size_t n;
	FILE *file;
	ssize_t nread, num;

	if (argc != 2)
		exit(EXIT_FAILURE);
	file = fopen(argv[1], "r");
	if (file == NULL)
		exit(EXIT_FAILURE);
	while ((nread = getline(&lineptr, &n, file)) != -1)
	{
		number = strtok(lineptr, " ");
		num = strtoll(number, &endptr, 10);
		printf("%ld\n", sqrtl(num));
	}
	return (0);
}
