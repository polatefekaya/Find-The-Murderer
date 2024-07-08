For the fear test, the friends go to a secluded place together and walk around in groups. In the process, the friends see each other and remember who they saw. After the test, one person is found lifeless. It is known that there is a murder and that the murder has an assistant. The killer is also thought to have an assistant. The group asks for your help to find the culprit.

If a person has been seen by 2 or more people, he is considered clean, otherwise he is considered a suspect. You must forward a list of all suspects to the group

Input
The first line contains the number Q of the test case. 1 ≤ Q ≤ 10000 The next Q input lines and each line contains a sequence of 0|1s of length Q. 1s mean they have seen it and 0s mean they have not seen it. 2 are marked so that they see their place in the array.

Output
Print the entire list of suspects in one line

Examples

Input
3
2 1 1
1 2 0
1 0 2

Output
1 2 

Input
4
2 1 1 0
1 2 0 1
1 0 2 1
0 1 1 2

Output

Note
Example 1: There are 3 people in the first example. Since 2 is first, we first evaluate the first person with index 0. He says he saw children with index 1 and 2.
The person with index 1 says that they saw index 0 but not index 2.
Person with index 2: saw index 0 but not index 1.

Example 2: Everyone has been seen by 2 people so there are no suspects in the group 
