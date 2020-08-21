/*
author Harsha Gupta
Function with fixed N (needs to be changed)
*/



#include<iostream> 
using namespace std; 

// Number of persons (or vertices in the graph) 
#define N 3 
// A utility function that returns index of minimum value in arr[] 
int getMin(int arr[]) 
{ 
	int minInd = 0; 
	for (int i=1; i<N; i++) 
		if (arr[i] < arr[minInd]) 
			minInd = i; 
	return minInd; 
} 

// A utility function that returns index of maximum value in arr[] 
int getMax(int arr[]) 
{ 
	int maxInd = 0; 
	for (int i=1; i<N; i++) 
		if (arr[i] > arr[maxInd]) 
			maxInd = i; 
	return maxInd; 
} 

// A utility function to return minimum of 2 values 
int minOf2(int x, int y) 
{ 
	return (x<y)? x: y; 
} 


void minCashFlowRec(int amount[]) 
{ 

	int mxCredit = getMax(amount), mxDebit = getMin(amount); 

	// If both amounts are 0, then all amounts are settled 
	if (amount[mxCredit] == 0 && amount[mxDebit] == 0) 
		return; 

	int min = minOf2(-amount[mxDebit], amount[mxCredit]); 
	amount[mxCredit] -= min; 
	amount[mxDebit] += min; 

	// If minimum is the maximum amount to be 
	cout << "Person " << mxDebit << " pays " << min 
		<< " to " << "Person " << mxCredit << endl; 

	minCashFlowRec(amount); 
} 


void minCashFlow(int graph[][N]) 
{ 
	// Create an array amount[], initialize all value in it as 0. 
	int amount[N] = {0}; 

	for (int p=0; p<N; p++) 
	for (int i=0; i<N; i++) 
		amount[p] += (graph[i][p] - graph[p][i]); 

	minCashFlowRec(amount); 
} 

int main() 
{ 
	string name;
	cout<<"ENTER NO OF FRIENDS:"<<"   "<<N<<endl;
	cout<<"Enter Names !"<<endl<<"Your friends will get an assigned no. by us!"<<endl;

	for(int i=0;i<N;i++)
	{
		cout<<"friend"<<i<<":"<<"  ";
		cin>>name;
		cout<<endl;
	}
	int graph[N][N] ;
	for(int i=0;i<N;i++)
	{
		cout<<"friend  "<<i<<"  gave to friend 0,1,2.. in order : "<<endl;
		for(int j=0;j<N;j++)
		{
					cin>>graph[i][j];
				

		}
	}
	

	minCashFlow(graph); 
	return 0; 
} 
