#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 *infinite_while - creates infinite loop
 *Return: always 0
 */
int infinite_while(void)
{
while (1)
{
sleep(1);
}
return (0);
}
/**
 * main - For every zombie process created, it displays
 * Return: always 0
 */
int main(void)
{
int index = 0;
pid_t zomb;
while (index < 5)
{
zomb = fork();
if (!zomb)
return (0);
printf("Zombie process created, PID: %d\n", zomb);
index++;
}
infinite_while();
return (0);
}
