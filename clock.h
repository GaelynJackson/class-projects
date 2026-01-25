//ChadaTechClocks by Gaelyn Jackson
//1-22-2026
//Header.h for ChadaTechClocks

//this inline guard will keep from erros in declaring header in both source.cpp files 
#ifndef CLOCK_H            
#define CLOCK_H

//allows user input
#include <iostream>
//allows the use of setw 
#include <iomanip>
//uses real time 
#include <ctime>
//allows using string
#include <string>

//shows the 12 and 24 hour clocks
void displayClocks(int hour, int minute, int second);

//shows the menu
void displayMenu();

//accepts what option the user types in the menu
int userOption();

//runs the user option selected
void runUserOption(int option, int& hour, int& minute, int& second);

//adds one hour
void addOneHour(int& hour);

//adds one minute
void addOneMinute(int& hour, int& minute);

//adds one second
void addOneSecond(int& hour, int& minute, int& second);

//ends include guard
#endif  