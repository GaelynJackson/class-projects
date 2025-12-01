//CatClass by Gaelyn Jackson
package pet;//Package for pet

public class CatClass {//Public class for Cat
	private String petType; //Attribute for pet type, this class is for cats
	private String petName; //Attribute for pet name
	private int petAge; //Attribute for pet age
	private int catSpaces; //Attribute for total number of cat spaces
	private int catSpaceNumber;//Attribute for assigned cat space
	private int daysStay; //Attribute for the number of days a pet stays
	private double amountDue; //Attribute for amount due
	
	public CatClass () {//Constructor, will be empty 
		
	}
	
	public String getPetType() {
		return petType;//Getter for pet type
	}
	
	public String getPetName() {
		return petName;//Getter for pet name
	}
	
	public int getPetAge() {
		return petAge;//Getter for pet age
	}
	
	public int getCatSpaces() {
		return catSpaces;//Getter for total cat spaces
	}
	
	public int getCatSpaceNumber() {
		return catSpaceNumber;//Getter for assigned cat space
	}
	
	public int getDaysStay() {
		return daysStay;//Getter for total number of days stayed
	}
	
	public double getAmountDue() {
		return amountDue;//Getter for amount due
	}
	
	public void setPetType(String petType) {
		this.petType = petType;//Setter for pets type
	}
	
	public void setPetName(String petName) {
		this.petName = petName;//Setter for pets name
	}
	
	public void setPetAge (int petAge) {
		this.petAge = petAge;//Setter for pet age
	}
	
	public void setCatSpaces(int catSpaces) {
		this.catSpaces = catSpaces;//Setter for total cat spaces
	}
	
	public void setCatSpacesNumber(int catSpaceNumber) {
		this.catSpaceNumber = catSpaceNumber;//Setter for assigned cat space
	}
	
	public void setDaysStay(int daysStay) {
		this.daysStay = daysStay;//Setter for number of days a cat stays
	}
	
	public void setAmountDue(double amountDue) {
		this.amountDue = amountDue;//Setter for total due
	}
}
