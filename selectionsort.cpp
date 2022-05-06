// C++ program for implementation of selection sort
#include <stdio.h>
#include <iostream>
using namespace std;

void swap(int *x, int *y)
{
	int temp = *x;
	*x = *y;
	*y = temp;
}

void selectionSort(int arr[], int n)
{
	int i, j, min;

	// One by one move boundary of unsorted subarray
	for (i = 0; i < n-1; i++)
	{
		min = i;
		for (j = i+1; j < n; j++)
		if (arr[j] < arr[min])
			min = j;

		// Swap the found minimum element with the first element
		swap(&arr[min], &arr[i]);
	}
}

void printarray(int arr[], int size)
{
	int i;
	for (i=0; i < size; i++)
		printf("%d ",arr[i]);
}
int main()
{
	int arr[] = {77,99,7,5,94,62,4,35,56,21};
	int n = sizeof(arr)/sizeof(arr[0]);
    int i;
    printf("Unsorted Array: \n");
    printarray(arr,n);
	selectionSort(arr, n);
	printf("\nSorted array: \n");
	printarray(arr, n);
	printf("\nMade by Himanshu Balani");
	return 0;
}
