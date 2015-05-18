#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
	cout << "hello world"<<endl;
	cout <<left;
	for(int i=0;i!=10;i++)
	{
		cout << setw(4)<< i;
	}
	
	return 0;
}