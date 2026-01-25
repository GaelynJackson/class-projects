//ChadaTechClocks by Gaelyn Jackson
//1-22-2026
//main() for ChadaTechClocks program

//applies header functions
#include "clock.h"

using namespace std;

//main
int main() {
//for this I will use 11 for hours, 58 for minutes, and 59 for seconds. 
//this will demonstrate that if the user types 3, the clock will reset seconds and increase the minute by one
//next if the user types 2, the minutes will reset to 0 and increase hour by one
//the user should then notice that the clock now will show PM instead of AM
	int hour = 11; //stores the hour in 24-hour format
	int minute = 58; //stores the minute
	int second = 59; //stores the second
	int option = 0; //stores menu option

	//loop that will run until user types 4
	while (option != 4) {
		displayClocks(hour, minute, second); //shows 12-hour and 24-hour clocks
		displayMenu(); //shows menu
		option = userOption(); //takes what option user typed 
		runUserOption(option, hour, minute, second);
	}

	return 0; //ends program
}