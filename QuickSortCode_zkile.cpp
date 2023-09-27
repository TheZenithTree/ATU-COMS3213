// QuickSortCode_zkile.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
using namespace std;

void swap(int& a, int& b)
{
    int temp;
    temp = a;
    a = b;
    b = temp;
}

int partition(int arr[], int begin, int end)
{
    int pivot = arr[end];
    int i = begin - 1;

    for (int j = begin; j < (end); j++)
    {
        if (arr[j] >= pivot)
        {
            i += 1;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[end]);

    return i + 1;
}


void quickSort(int arr[], int begin, int end)
{
    int partIndex;

    if (begin >= end)
        return;

    partIndex = partition(arr, begin, end);
    quickSort(arr, begin, (partIndex - 1));
    quickSort(arr, (partIndex + 1), end);
}


void output(int arr[], int length)
{
    for (int i = 0; i < length; i++)
    {
        cout << arr[i] << " ";
    }

    cout << endl;
}

int main()
{
    int array[10] = {9, 5, 6, 10, 34, 13, 20, 59, 21, 0};
    int length = sizeof(array) / sizeof(array[0]);
    quickSort(array, 0, length);

    output(array, length);

    return 0;
}

