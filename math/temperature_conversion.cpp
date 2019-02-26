/* Author: Aiswarya Jayachandran (https://github.com/Aishh2k)
   C++ Program - Temperature Converter between Fahrenheit and Celsius*/


#include<iostream.h>
#include<conio.h>
void main()
{
	clrscr();
	float fah, cel;
	int choice;
        cout<<"Main menu"<<endl;
	cout<<"1.Fahrenheit to Celsius"
	cout<<endl<<"2.Celsius to Fahrenheit"
	cout<<endl<<"Enter choice: "
	cin>>choice;
              if (choice==1)
	         {
			cout<<"Enter temperature in Fahrenheit : ";
			cin>>fah;
			cel=(fah-32) / 1.8;
			cout<<"Temperature in Celsius = "<<cel;
	
                 }
	      
              else if (choice==2)
                 {
                        cout<<"Enter temperature in Celsius : ";
	                cin>>cen;
	                fah=(1.8 * cen) + 32;
	                cout<<"\nTemperature in Fahrenheit = "<<fah;
                 }

              else
                cout<<"Invalid option";   
        getch();

}
