#include <stdio.h>
#include <stdlib.h>

int main(void) {
    // Print Intro
    printf("This This is a preview of how printing.py is supposed to be like. \n");
    printf("Remember, your program does not exactly have to be like this program! \n\n");
    
    // Body
    char str1[100], str2[100];
    printf("Please input your first number to add: ");
    fgets(str1, sizeof(str1), stdin);
    printf("Please input your second number to add: ");
    fgets(str2, sizeof(str2), stdin);
    int num1 = atoi(str1);
    int num2 = atoi(str2);
    printf("Your sum is %d.\n\n", num1 + num2);

    // Print Outro
    printf("End of program. Press enter to exit preview \n");
    getchar();
}