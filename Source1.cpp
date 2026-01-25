//ChadaTechClocks by Gaelyn Jackson
//1-22-2026
//The purpose of this program is to display a 12-hour and 24-hour clock and both will display at once
//The user will also be able to add one hour, one minute, and one second to each clock by interacting with a menu and will be able to close the application by typing the appropriate number
//This will call the header and the functions I created within it

//allows using cin and cout for user input and showing output
#include <iostream>
//allows using setw 
#include <iomanip>
//allows using string
#include <string>
//uses header functions
#include "clock.h"

using namespace std;

//uses 12 hour clock and stores if AM or PM
void displayClocks(int hour, int minute, int second) {
	int hour12 = hour;
	string time = "AM";

	//will use PM if noon (12:00PM) or later
	if (hour12 >= 12) {
		time = "PM";
	}

	//will use AM if midnight or earlier (until 11:59AM)
	if (hour12 == 0) { //0 represents midnight
		hour12 = 12; //shows 0 as 12AM
	}
	else if (hour12 > 12) { //for 24 hour clock if the number is above 12
		hour12 -= 12; //will convert 24 hour into 12 hour by subtracting 12 from the current number
	}

	//graphic boarder for both clocks
	cout << "*************************     *************************\n"; //starts the top of the boarder for the clocks, will start a newline 
	cout << "*       12-Hour Clock    *     *       24-Hour Clock    *\n"; //starts a newline once finshed, lets users know which clock is for 12 and 24 hours
	cout << "*       "
		<< setw(2) << setfill('0') << hour12 << ":" // 12-hour clock hours
		<< setw(2) << minute << ":"                 // 12-hour clock minutes
		<< setw(2) << second << " " << time          // 12-hour clock seconds in AM or PM
		<< "       *     *       "
		<< setw(2) << hour << ":"                    // 24-hour clock hours
		<< setw(2) << minute << ":"                  // 24-hour clock minutes
		<< setw(2) << second                          // 24-hour clock seconds in AM or PM
		<< "       *\n"; //starts a newline
	cout << "*************************     *************************\n\n"; //closes the boarder for the clocks and starts a newline
}

//shows the menu users can interact with
void displayMenu() {
	cout << "*************************\n"; //starts menu boarder and newline
	cout << "* 1 - Add One Hour      *\n"; //option 1 and newline
	cout << "* 2 - Add One Minute    *\n"; //option 2 and newline
	cout << "* 3 - Add One Second    *\n"; //option 3 and newline
	cout << "* 4 - Exit Program      *\n"; //option 4 and newline
	cout << "*************************\n"; //closes menu boarder
}

int userOption() {
	int option; //keeps the user input
	cout << "Please type a number: "; //tells user to type a number from the menu
	cin >> option;
	return option; //returns what the user typed
}

void runUserOption(int option, int& hour, int& minute, int& second) { //using int& lets the int variable be modified
	switch (option) { //will run different function based on what user typed in the menu
	case 1:
		addOneHour(hour); //calls addOneHour
		break;
	case 2:
		addOneMinute(hour, minute); //calls addOneMinute
		break;
	case 3:
		addOneSecond(hour, minute, second); //calls addOneSecond
		break;
	case 4:
		cout << "Exiting program, goodbye!\n"; //shows goodbye message
		break;
	default:
		cout << "Please type a valid option\n"; //shows if user types in anything other than 1,2,3,or 4
	}
}

//will increase hour by one
void addOneHour(int& hour) { //using int& lets the int variable in hour be modified 
	hour++;
	if (hour == 24) { //if the time is midnight, than the time will show 0
		hour = 0; //midnight is 0
	}
}

//will increase minute by one
void addOneMinute(int& hour, int& minute) { //using int& lets the int variable in minute be modfied 
	minute++;
	if (minute == 60) { //if minutes is 60, then the minutes reset to 0, since 60 minutes == 1 hour
		minute = 0;
		addOneHour(hour); //will increas the hour if minutes == 60
	}
}

//will increase second by one
void addOneSecond(int& hour, int& minute, int& second) { //using int& lets the int variable in second be modified
	second++;
	if (second == 60) { //if seconds is 60, then seconds reset and minute increases, since 60 seconds == 1 minute
		second = 0;
		addOneMinute(hour, minute);
	}
}