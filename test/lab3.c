#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int i = 0;
void E(),EDash(),T(),TDash(),F(),advance(),error();

int main()
{
    char str[50];
    printf("Enter the string : ");
    scanf("%s",str);
    int len = strlen(str);
    E(str);

    if(i == len){
        printf("Accepted\n");
    }
    else
    {
        printf("Rejected\n");
    }

    return 0;
}

void advance(){
    i++;
}

void error(){
    printf("Rejected");
    exit(0);
}

void F(char str[]){
    if(str[i] == '('){
        advance();
        E(str);
        if(str[i] == ')'){
            advance();
        }
        else{
            error();

        }
    }
    else if(str[i] == 'i'){
        advance();
    }
    else{
        error();
    }
}

void TDash(char str[]){
    if(str[i] == '*'){
        advance();
        T(str);
        TDash(str);
    }
}

void T(char str[]){
    F(str);
    TDash(str);
}

void EDash(char str[]){
    if(str[i] == '+'){
        advance();
        T(str);
        EDash(str);
    }
}

void E(char str[]){
    T(str);
    EDash(str);
}