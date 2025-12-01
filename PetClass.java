//PetClass by Gaelyn Jackson
package pet;//Package for pet

public class PetClass {//Public class for pets
	private String petType; //Will store information on if the pet is a cat or dog
	private String petName; //Will store a pet's name
	private int petAge; //Will store the age of a pet
	private int dogSpaces; //Will store the open spaces for dogs
	private int catSpaces; //Will store the open spaces for cats
	private int daysStay; //Will store the total days a pet will be boarding
	private double amountDue; //Will store what the total cost for a pet's stay

public PetClass() {//Default constructor, values are empty or 0
		petType = ""; //Constructor for type of pet
		petName = ""; //Constructor for pet name
		petAge = 0; //Constructor for pet age
		dogSpaces = 0; //Constructor for spaces for dogs
		catSpaces = 0; //Constructor for spaces for cats
		daysStay = 0; //Constructor for pet's total days boarded
		amountDue = 0; //Constructor for total amount due
	}


public PetClass(String petType, String petName, int dogSpaces, int catSpaces,int daysStay, double amountDue ) {
		this.petType = petType; //Assigns a pet type
		this.petName = petName; //Assigns a pet name
		this.petAge = 0; //When age not given, defaults to 0
		this.dogSpaces = dogSpaces; //Assigns a value to open dog spaces
		this.catSpaces = catSpaces; //Assigns a value to open cat spaces
		this.daysStay = daysStay; //Assigns the number of days a pet stays
		this.amountDue = amountDue; //Assigns a value for amount due
	}


public String getPetType() {
		return petType; //Getter for pet type (cat or dog)
	}

public String getPetName() {
		return petName; //Getter for pet name
	}

public int getPetAge() {
		return petAge; //Getter for pet age
	}

public int getDogSpaces() {
		return dogSpaces; //Getter for open dog spaces
	}

public int getCatSpaces() {
		return catSpaces; //Getter for open cat spaces
	}

public int getDaysStay() {
		return daysStay; //Getter for total days a pet stayed
	}

public double getAmountDue() {
		return amountDue; //Getter for total amount due
	}


public void setPetType(String petType) {
		this.petType = petType; //Setter for pet type
	}

public void setPetName(String petName) {
		this.petName = petName; //Setter for pet name
	}

public void setPetAge(int petAge) {
		this.petAge= petAge; //Setter for pet age
	}

public void setDogSpaces(int dogSpaces) {
		this.dogSpaces = dogSpaces; //Setter for number of dog spaces
	}

public void setCatSpaces(int catSpaces) {
		this.catSpaces = catSpaces; //Setter for number of cat spaces
	}

public void setDaysStay(int daysStay) {
		this.daysStay = daysStay; //Setter for total days a pet stayed
	}

public void setAmountDue(double amountDue) {
		this.amountDue = amountDue; //Setter for total due
	}
}
