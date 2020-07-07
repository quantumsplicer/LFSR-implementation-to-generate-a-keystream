# LFSR-implementation-to-generate-a-keystream

I wrote a code which uses the LFSR method to generate a keystream that can be further used to encode a message.

In the code first of all the user gives an input for the seed value of the LFSR and the taps that the user wants to be used. (A good LFSR output may be received if even number of taps are used and all the taps are coprime, though this does not ensure the maximum possible non-repetitive length of the output stream. ) The user also inputs the length of the output stream required.

The main function takes all these inputs and then passes them to the LFSR function. 

Inside the LFSR function, on each iteration of the loop, for the seed value, the bits on all positions corresponding to individual values of taps are xored and the result is appended at the start of the previous seed variable value with each bit shifted by one position to the right. The stream variable is defined which stores and appends the value of the last bit of the seed variable each time its value is changed.
The above step is looped till the length of the stream is as required by the user. The stream is finally printed out as an output.

